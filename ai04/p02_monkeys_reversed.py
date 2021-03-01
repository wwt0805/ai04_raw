

def get_peaches(monkeys):
    unit = 1
    while True:
        ok, peaches = divide((monkeys-1) * unit, monkeys)
        if ok:
            return peaches
        unit += 1


def divide(peaches, monkeys):
    for _ in range(monkeys):
        if peaches % (monkeys - 1) == 0:
            peaches = peaches // (monkeys - 1) * monkeys + 1
        else:
            return False, 0
    return True, peaches



print(get_peaches(6))