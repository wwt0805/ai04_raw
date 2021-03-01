def solve():
    # y = lambda x1, x2: (x1 - 3) ** 2 + (x2 + 2) ** 2

    dy_dx1 = lambda x1, x2: 2 * (x1 - 3)
    dy_dx2 = lambda x1, x2: 2 * (x2 + 2)

    dx = lambda x1, x2, lr: (-lr * dy_dx1(x1, x2), -lr * dy_dx2(x1, x2))
    x1, x2 = 1, 1
    lr = 0.01

    for _ in range(2000):
        d1, d2 = dx(x1, x2, lr)
        x1 += d1
        x2 += d2

    return x1, x2

print(solve())  # 3, -2

# y = -3 x^4 + 20 x^2 +10 x + 9