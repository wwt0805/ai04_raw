
import math


class Exp:
    def deriv(self, x):
        pass

    def eval(self):
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

    def eval(self):
        return self.value

    def __repr__(self):
        return str(self.value)

    def get_vars(self):
        return set()  # {}

def to_exp(value):
    return value


class Session:
    default_session = None

    def __init__(self):
        self.map = {}

    def set(self, x, value):
        self.map[x] = value

    def get(self, x):
        return self.map[x]

    def contains(self, x):
        return x in self.map




class Variable(Exp):
    def __init__(self, name):
        self.name = name

    def deriv(self, x):
        return Const(1) if self is x else Const(0)

    def eval(self):
        if Session.default_session.contains(self):
            return Session.default_session.get(self)
        raise Exception('Variable %s is not found.' % self.name)

    def __repr__(self):
        return str(self.name)

    def get_vars(self):
        return {self}



if __name__ == '__main__':
    session = Session()
    x = Variable('x')
    c = Const(123)
    y = x

    Session.default_session = session

    Session.default_session.set(x, 999)
    print(y.eval())
