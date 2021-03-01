

def get_peaches(monkeys):
    p = 1
    while not dividable(p, monkeys):
        p += monkeys    # p = p+1
    return p


def dividable(p, m):
    for _ in range(m):
        p -= 1  # p = p-1
        if p % m == 0:
            p = p // m * (m - 1)
        else:
            return False
    return True


print(get_peaches(7))
