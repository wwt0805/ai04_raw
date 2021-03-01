

def get_trains(n):
    if n <= 1:
        return 1
    result = 0
    for i in range(n):
        result += get_trains(i) * get_trains(n - 1 - i)
    return result


for n in range(15+1):
    print('get_trains(%d) = %d' % (n, get_trains(n)))