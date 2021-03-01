

def fac(n):
    result = [1]   # result = 1
    while n > 1:
        mul(result, n)  # result *= n
        n -= 1
    return to_str(result)  # return result


def mul(result, n):
    add = 0
    for i in range(len(result)):
        r = n * result[i] + add
        result[i] = r % 10
        add = r // 10
    while add > 0:
        result.append(add % 10)
        add //= 10


def to_str(result):
    s = ''
    for e in result:
        s = str(e) + s
    return s

for n in range(1, 100+1):
    print('%d! = %s' % (n, fac(n)))