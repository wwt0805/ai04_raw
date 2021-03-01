class ABC:  # 封装
    def m1(self):
        print(self.a)

    def m2(self):
        print(self.b)

o1 = ABC()
o2 = o1
o3 = ABC()

o1.a = 123
o2.a = 321
o1.m1()
o2.m1()

o3.a = 456
o3.m1()


class DEF(ABC): # 继承
    def m1(self):
        print('Welcome!')


o4 = DEF()
o4.a = 678
o4.m1()


class Viecle:
    def get_foots(self):
        return 4

    def get_price(self):
        return self.get_foots() ** 2

class Trunck(Viecle):
    def get_foots(self):  # override  overload
        return 8

v1 = Viecle()
v2 = Trunck()

print(v1.get_foots())
print(v2.get_foots())
print(v1.get_price())
print(v2.get_price())


print('-' * 200)

class A:
    def __add__(self, other):
        print('in __add__()')
        print(other)

    def __sub__(self, other):
        pass

    def __str__(self):
        print("in __str__()")
        return '123'

    def __repr__(self):
        print('in repr')
        return 'ddd'

    def __reversed__(self):
        print('in __reversed__()')

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __divmod__(self, other):  # ?
        print('in divmod')

    def __idiv__(self, other):   # ?
        print('in idiv')

    def __pow__(self, power, modulo=None): # **
        pass

    def __neg__(self):  # -
        print('in neg')

    def __xor__(self, other):  # ^
        pass

    def __or__(self, other):   # |
        pass

    def __and__(self, other):  # &
        pass

    def __invert__(self):   # ~
        print('in invert')

    def __mod__(self, other):  # %
        print('in mod')

    def __lshift__(self, other):  # <<
        print('in lshift')

    def __rshift__(self, other):  # >>
        print('in rshift')

    def __radd__(self, other):
        print('in radd')


a = A()
b = a + 3  # a.__add__(3)
print(b)

b = a - 3 # a.__sub__(3)
b = a * 3 # a.__mul__(3)
b = a / 3 # a.__truediv__(3)
# b = a // 3 # a.__divmode__(3)
b = a ** 3
b = -a
b = ~a
b = a % 3 # a.__mod__(3)
b = a << 3
b = a >> 3
b = str(a)
b = reversed(a)
print(a)

b = a and 3

b = 3 + a  # a.__radd__(3)