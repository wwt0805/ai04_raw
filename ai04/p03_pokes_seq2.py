

def get_pokes(num):
    result = [0] * num
    loc = [e  for e in range(num)]
    for p in range(1, num):
        move(p, result, loc)
    result[loc[0]] = num
    return result

def move(p, result, loc):
    first = loc[0]
    del loc[0]
    result[first] = p
    for _ in range(p):
        first = loc[0]
        del loc[0]
        loc.append(first)


print(get_pokes(20))