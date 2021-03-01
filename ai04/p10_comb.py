"""
C(5, 2) = 10
C(6, 3) = 20
C(4, 2) = 6

C(n, m) = ?   0 <= m <= n
"""

def comb(n, m):
    if m == 0 or m == n:
        return 1
    if m == 1:
        return n
    return comb(n-1, m-1) + comb(n-1, m)

def combinations(ns, m):
    ns = tuple(ns)
    if m == 0:
        return [()]
    if m == len(ns):
        return [ns]
    if m == 1:
        return [(n,) for n in ns]
    first = ns[0]
    result = combinations(ns[1:], m-1)
    result = [(first,) + r for r in result]
    return result + combinations(ns[1:], m)


def combinations2(ns, m, store=None):
    ns = tuple(ns)
    if m == 0:
        return [()]
    if m == len(ns):
        return [ns]
    if m == 1:
        return [(n,) for n in ns]

    if store is None:
        store = {}
    key = (ns, m)
    if key in store:
        return store[key]

    first = ns[0]
    result = combinations2(ns[1:], m-1, store)
    result = [(first,) + r for r in result]
    result += combinations2(ns[1:], m, store)

    store[key] = result
    return result

# for n in range(1, 10+1):
#     for m in range(n+1):
#         print('C(%d, %d) = %d' % (n, m, comb(n, m)))

for n in range(1, 10+1):
    for m in range(n+1):
        print('C(%d, %d) = %s' % (n, m, combinations2([e for e in range(n)], m)))
