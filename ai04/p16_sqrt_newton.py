


def sqrt(a, n=2):
    # return: a ** (1/n)
    x = 1
    y = lambda x: x**n
    # def y(x):
    #     return x**n

    dy_dx = lambda x: n * x**(n-1)
    delta_y = lambda x: a - y(x)
    delta_x = lambda x: delta_y(x) / dy_dx(x)

    # dx = dy / y' = (a - x**2) / 2x
    # x' = x + dx = (a + x**2)/2x
    # x' = x + dx = x + (a - x**3)/(3x**2) =(a + 2*x**3)/(3x**2)

    for _ in range(10):
        x += delta_x(x)
    return x


for x in range(1, 10+1):
    print('sqrt(%s) = %s' % (x, sqrt(x, 2.5)))