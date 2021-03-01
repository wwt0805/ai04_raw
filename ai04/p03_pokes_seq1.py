

def get_pokes(num):
    result = [0] * num
    loc = 0
    for p in range(1, num):
        loc = insert(p, result, loc)
    result[loc] = num
    return result

def insert(p, result, loc):
    result[loc] = p
    num = len(result)
    for _ in range(p + 1):
        while True:
            loc = (loc + 1) % num
            if result[loc] == 0:
                break
    return loc

print(get_pokes(20))