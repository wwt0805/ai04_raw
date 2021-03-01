import math

def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):    # a   2, 3, 4, ...., sqrt(a), sqrt(a) + 1
        if x % i == 0:
            return False
    return True


n = 1000
for x in range(2, n+1):
    if is_prime(x):
        print(x, end=', ')
