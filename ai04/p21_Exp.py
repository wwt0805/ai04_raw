
import math


class Exp:
    def deriv(self, x):
        pass

    def eval(self, env:dict):
        pass

    def simplify(self):
        return self

    def get_vars(self):
        pass

    # def add(self, other):
    #     other = to_exp(other)
    #     return Add(self, other).simplify()

    def __add__(self, other):
        other = to_exp(other)
        return Add(self, other).simplify()

    def __radd__(self, other):
        other = to_exp(other)
        return Add(other, self).simplify()

    def __sub__(self, other):
        other = to_exp(other)
        return Sub(self, other).simplify()

    def __rsub__(self, other):
        other = to_exp(other)
        return Sub(other, self).simplify()

    def __mul__(self, other):
        other = to_exp(other)
        return Mul(self, other).simplify()

    def __rmul__(self, other):
        other = to_exp(other)
        return Mul(other, self).simplify()

    def __neg__(self):
        return Neg(self).simplify()

    def __truediv__(self, other):
        other = to_exp(other)
        return Truediv(self, other).simplify()

    def __rtruediv__(self, other):
        other = to_exp(other)
        return Truediv(other, self).simplify()

    def __pow__(self, power, modulo=None):
        power = to_exp(power)
        return Pow(self, power).simplify()

    def __rpow__(self, other):
        other = to_exp(other)
        return Pow(other, self).simplify()

    def __abs__(self):
        return Abs(self).simplify()

    def __gt__(self, other):
        other = to_exp(other)
        return Gt(self, other).simplify()


class Const(Exp):
    def __init__(self, value):
        self.value = value

    def deriv(self, x):
        return Const(0)

    def eval(self, env:dict):
        return self.value

    def __repr__(self):
        return str(self.value)

    def get_vars(self):
        return set()  # {}


class Variable(Exp):
    def __init__(self, name):
        self.name = name

    def deriv(self, x):
        return Const(1) if self is x else Const(0)

    def eval(self, env:dict):
        if self in env:
            return env[self]
        raise Exception('Variable %s is not found.' % self.name)

    def __repr__(self):
        return str(self.name)

    def get_vars(self):
        return {self}


def to_exp(v):
    if isinstance(v, Exp):
        return v
    return Const(v)


class Binary(Exp):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return '(%s %s %s)' % (self.left, self.get_op(), self.right)

    def get_op(self):
        raise Exception('get_op() is not defined')

    def get_vars(self):
        return self.left.get_vars().union(self.right.get_vars())


class Add(Binary):
    def deriv(self, x):
        return self.left.deriv(x) + self.right.deriv(x)

    def eval(self, env):
        return self.left.eval(env) + self.right.eval(env)

    def get_op(self):
        return '+'

    def simplify(self):
        if isinstance(self.left, Const):
            if self.left.value == 0:
                return self.right
            if isinstance(self.right, Const):
                return Const(self.left.value + self.right.value)
        elif isinstance(self.right, Const) and self.right.value == 0:
            return self.left
        return self


class Sub(Binary):
    def deriv(self, x):
        return self.left.deriv(x) - self.right.deriv(x)

    def eval(self, env):
        return self.left.eval(env) - self.right.eval(env)

    def get_op(self):
        return '-'

    def simplify(self):
        if isinstance(self.left, Const):
            if self.left.value == 0:
                return -self.right
            if isinstance(self.right, Const):
                return Const(self.left.value - self.right.value)
        elif isinstance(self.right, Const) and self.right.value == 0:
            return self.left
        return self


class Mul(Binary):
    def deriv(self, x):
        # (uv)' = uv' + u'v
        u = self.left
        v = self.right
        return u * v.deriv(x) + u.deriv(x) * v

    def eval(self, env):
        return self.left.eval(env) * self.right.eval(env)

    def get_op(self):
        return '*'

    def simplify(self):
        if isinstance(self.left, Const):
            if self.left.value == 0:
                return Const(0)
            if self.left.value == 1:
                return self.right
            if isinstance(self.right, Const):
                return Const(self.left.value * self.right.value)
        elif isinstance(self.right, Const):
            if self.right.value == 0:
                return Const(0)
            if self.right.value == 1:
                return self.left
        return self


class Unary(Exp):
    def __init__(self, value):
        self.value = value

    def get_vars(self):
        return self.value.get_vars()

    def __repr__(self):
        return self.get_pattern() % (self.value)

    def get_pattern(self):
        pass

    def simplify(self):
        return self.get_value(self.value.value) if isinstance(self.value, Const) else self

    def get_value(self, python_value):
        pass


class Neg(Unary):
    def get_pattern(self):
        return '(-%s)'

    def deriv(self, x):
        return - self.value.deriv(x)

    def eval(self, env):
        return - self.value.eval(env)

    def get_value(self, python_value):
        return -python_value


class Truediv(Binary):
    def deriv(self, x):
        # (u/v)' = (u'v - uv') / v**2
        u = self.left
        v = self.right
        return (u.deriv(x) * v - u * v.deriv(x)) / v**2

    def eval(self, env):
        return self.left.eval(env) / self.right.eval(env)

    def get_op(self):
        return '/'

    def simplify(self):
        if isinstance(self.left, Const):
            if self.left.value == 0:
                return Const(0)
            if isinstance(self.right, Const):
                return Const(self.left.value / self.right.value)
        elif isinstance(self.right, Const) and self.right.value == 1:
            return self.left
        return self


class Pow(Binary):
    def deriv(self, x):
        # (u**v)' = (v’ln(u) + v u’/u) * y
        u = self.left
        v = self.right
        return (v.deriv(x) * log(u) + v * u.deriv(x)/u) * self

    def eval(self, env):
        return self.left.eval(env) ** self.right.eval(env)

    def get_op(self):
        return '**'

    def simplify(self):
        if isinstance(self.left, Const):
            if self.left.value in (0, 1):
                return Const(self.left.value)
            if isinstance(self.right, Const):
                return Const(self.left.value ** self.right.value)
        elif isinstance(self.right, Const):
            if self.right.value == 0:
                return Const(1)
            if self.right.value == 1:
                return self.left
        return self


e = Const(math.e)
pi = Const(math.pi)
one = Const(1)
zero = Const(0)


def log(value, base=e):
    value = to_exp(value)
    base = to_exp(base)
    return Log(value, base).simplify()


class Log(Exp):
    def __init__(self, value, base=e):
        self.value = value
        self.base = base

    def __repr__(self):
        return 'log(%s)' % (self.value if self.base is e else ('%s, %s' % (self.value, self.base)))

    def simplify(self):
        if isinstance(self.value, Const):
            if self.value.value == 1:
                return zero
            if isinstance(self.base, Const):
                return math.log(self.value.value, self.base.value)
        return self

    def eval(self, env):
        return math.log(self.value.eval(env), self.base.eval(env))

    def deriv(self, x):
        # (log(u, v))' = (ln(u) / ln(v))' = (u'ln(v)/u - ln(u)v'/v)/ln(v)**2
        u = self.value
        v = self.base
        return (u.deriv(x) * log(v)/u - log(u) * v.deriv(x)/v)/log(v)**2

    def get_vars(self):
        return self.value.get_vars().union(self.base.get_vars())


def sin(value):
    value = to_exp(value)
    return Sin(value).simplify()


class Sin(Unary):
    def get_pattern(self):
        return 'sin(%s)'
    
    def eval(self, env):
        return math.sin(self.value.eval(env))
    
    def get_value(self, python_value):
        return math.sin(python_value)
    
    def deriv(self, x):
        return cos(self.value) * self.value.deriv(x)


def cos(value):
    value = to_exp(value)
    return Cos(value).simplify()


class Cos(Unary):
    def get_pattern(self):
        return 'cos(%s)'

    def eval(self, env):
        return math.cos(self.value.eval(env))

    def get_value(self, python_value):
        return math.cos(python_value)

    def deriv(self, x):
        return -sin(self.value) * self.value.deriv(x)


class Abs(Unary):
    def get_pattern(self):
        return '|%s|'

    def eval(self, env):
        return abs(self.value.eval(env))

    def get_value(self, python_value):
        return abs(python_value)

    def deriv(self, x):
        d = self.value.deriv(x)
        return cond(d, -d, self.value > 0)


def cond(true_value, false_value, cond):  # tf.cond
    true_value = to_exp(true_value)
    false_value = to_exp(false_value)
    cond = to_exp(cond)
    return Cond(true_value, false_value, cond).simplify()


class Cond(Exp):
    def __init__(self, true_value, false_value, condition):
        self.true_value = true_value
        self.false_value = false_value
        self.condition = condition

    def __repr__(self):
        return '(%s if %s else %s)' % (self.true_value, self.condition, self.false_value)

    def eval(self, env):
        c = self.condition.eval(env)
        if c:
            return self.true_value.eval(env)
        else:
            return self.false_value.eval(env)

    def simplify(self):
        c = self.condition
        if isinstance(c, Const):
            return self.true_value.simpify() if c.value else self.false_value.simplify()
        return self

    def get_vars(self):
        return self.true_value.get_vars().union(self.false_value.get_vars())

    def deriv(self, x):
        return Cond(self.true_value.deriv(x), self.false_value.deriv(x), self.condition)


class Gt(Binary):
    def get_op(self):
        return '>'

    def eval(self, env):
        return self.left.eval(env) > self.right.eval(env)

    def deriv(self, x):
        return zero

    def simplify(self):
        if isinstance(self.left, Const) and isinstance(self.right, Const):
            return self.left.value > self.right.value
        return self


if __name__ == '__main__':
    c1 = Const(123)
    print(c1)
    print(c1.deriv('x'))
    print(c1.eval(None))

    x = Variable('x')
    print(x)
    print(x.eval({x:12345}))
    print(x.deriv(x))

    e1 = x + c1
    print(e1, '=', e1.eval({x:456}))
    e2 = e1.deriv(x)
    print(e2, '=', e2.eval({x:100}))
    y = Variable('y')
    e2 = e1.deriv(y)
    print(e2, '=', e2.eval({x:100, y:200}))

    e3 = c1 + 400 - x
    print(e3)
    print(e3.deriv(x))

    e4 = c1 * x + 20 * x  # (c1 * x).add(20 * x)
    print(e4)
    print(e4.deriv(x))

    e5 = c1 * x / 20
    print(e5)
    print(e5.deriv(x))

    e6 = 3 * x**2 - 12 * x + pi
    print(e6)
    print(e6.deriv(x))

    e6 = x**5 + log(x**3)
    print(e6)
    print(e6.deriv(x))

    y = Variable('y')
    e7 = sin(x**2) + cos(y)**2 + sin(x*y)
    print(e7)
    print(e7.deriv(x))
    print(e7.deriv(y))
    print(e7.get_vars())

    e8 = abs(x**2 + 3*x - 12) + abs(x) ** 3
    print(e8)
    print(e8.deriv(x))