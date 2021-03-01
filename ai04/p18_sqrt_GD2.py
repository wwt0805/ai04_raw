
def sqrt(a, n=2):
    # y = lambda x: (x**n - a)**2
    dy_dx = lambda x: 2 * (x**n - a) * n * x**(n-1)
    dx = lambda x, lr: -lr * dy_dx(x)

    lr = 0.01
    x = 1.0
    for _ in range(1000):
        x += dx(x, lr)
    return x


for x in range(1, 10+1):
    print('sqrt(%s) = %s' % (x, sqrt(x)))