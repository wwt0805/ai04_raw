

def hanoi(src, mid, dst, num):
    if num == 1:
        # print('%s, %d ==> %s' % (src, 1, dst))
        pass
    else:
        hanoi(src, dst, mid, num - 1)
        # print('%s, %d ==> %s' % (src, num, dst))
        pass
        hanoi(mid, src, dst, num - 1)

def hanoi2(src, mid, dst, num, store=None):
    if num == 1:
        # print('%s, %d ==> %s' % (src, 1, dst))
        return
    if store is None:
        store = {}
    key = (src, mid, dst, num)
    if key in store:
        return store[key]

    hanoi2(src, dst, mid, num - 1, store)
    # print('%s, %d ==> %s' % (src, num, dst))
    pass
    hanoi2(mid, src, dst, num - 1, store)
    store[key] = None

for num in range(1, 400+1):
    print('-' * 50)
    print(num)
    hanoi2('A', 'B', 'C', num)
