"""
1   1
2   1
3   2
4   3
5   5
n   ?


20 --> 19, 18
19 --> 18, 17
18 --> 17, 16

"""


def get_rabbits(months):
    if months <= 2:
        return 1
    return get_rabbits(months - 1) + get_rabbits(months - 2)

def get_rabbits2(months, store:dict=None):   # dict: {'123': '张三'}
    if store is None:
        store = {}
    if months <= 2:
        return 1
    if months in store:
        return store[months]
    result = get_rabbits2(months - 1, store) + get_rabbits2(months - 2, store)
    store[months] = result
    return result

for months in range(1, 400+1):
    print(months, get_rabbits2(months))