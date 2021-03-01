
import math
def print_primes(n):
    #  1) tags = [2, 3, 4, ..., n]
    #  2) current = index + tags[index]
    #  3) tags = [2(tag), 3, 4(tag), 5, 7, ..., n]
    #  4) repeat index += 1 till tags[index] is not tagged.
    #  5) if current <= sqrt(n) then goto 2)
    #  6) print the elements that is not tagged in tags

    tags = [False for _ in range(2, n+1)]  # set all tag to False for all integers in range (2, n+1)
    index = 0
    value = 2
    sqrt = int(math.sqrt(n))
    while value <= sqrt:
        current = index + value
        while current < len(tags):
            tags[current] = True
            current += value
        while value <= sqrt:
            index += 1
            value += 1
            if not tags[index]: break

    for tag, value in zip(tags, range(2, n+1)):
        if not tag:
            print(value, end=', ')



print_primes(1000)