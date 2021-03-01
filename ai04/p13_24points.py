"""
2 5 7 11 == 24

"""
import numpy as np
#   python -m pip install numpy

import itertools as it

def get_numbers(num):
    return list(np.random.randint(1, 13+1, [num]))

def make(numbers, target):
    print(numbers)
    for value, exp in get_exps(numbers):
        if value == target:
            print(exp)

def get_exps(numbers):      # numbers = [2, 5, 7, 11]
    #  return:  [(25, '2+5+7+11'), (3, '2+5+7-11'), ...]
    if len(numbers) == 1:
        return [(numbers[0], str(numbers[0]))]

    result = []
    total = {e for e in range(len(numbers))}   # {0, 1, 2, 3}
    for left in range(1, len(numbers)):    # left = 1, 2, ... , n-1
        for left_ids in it.combinations(total, left):         # left_ids = {0}, {1}, {2}, {3}, {0, 1}, {0, 2}, {0, 3}, {1, 2}, {1, 3}, {2, 3}...
            right_ids = total - set(left_ids)                 # right_ids = {1, 2, 3}, {0, 2, 3}, {0, 1, 3}, {0, 1, 2}, {2, 3}, {0, 1}

            left_numbers = [numbers[i] for i in left_ids]     # [2], [5], [7], [11], ...
            right_numbers = [numbers[i] for i in right_ids]   # [5, 7, 11], [2, 7, 11], [2, 5, 7], ...

            for left_value, left_exp in get_exps(left_numbers):
                for right_value, right_exp in get_exps(right_numbers):
                    value = left_value + right_value
                    exp = '(%s + %s)' % (left_exp, right_exp)
                    result.append((value, exp))

                    value = left_value - right_value
                    exp = '(%s - %s)' % (left_exp, right_exp)
                    result.append((value, exp))

                    value = left_value * right_value
                    exp = '(%s * %s)' % (left_exp, right_exp)
                    result.append((value, exp))

                    if right_value != 0:
                        value = left_value / right_value
                        exp = '(%s / %s)' % (left_exp, right_exp)
                        result.append((value, exp))
    return result


numbers = get_numbers(4)
make(numbers, 24)
make([2, 5, 7, 11], 24)
make([3, 3, 7, 7], 24)



