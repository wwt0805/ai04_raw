
def get_pokes(num):
    result = [num]   # list
    p = num - 1
    while p > 0:
        insert(p, result)
        p -= 1
    return result


def insert(p, result):
    for _ in range(p):
        last = result[-1]
        del result[-1]
        result.insert(0, last)
    result.insert(0, p)


print(get_pokes(20))