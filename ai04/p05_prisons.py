import random

def solve_prisons(num):
    counter = num - 1
    turn_ons = [False] * (num - 1)
    lamp = False
    count = 0

    while True:
        lucky = random.randint(0, num-1)
        lamp, count = get_free(lucky, counter, turn_ons, lamp, count)
        if count == num - 1:
            break


def get_free(lucky, counter, turn_ons, lamp, count):
    if lucky == counter:
        if lamp:
            lamp = False
            count += 1
    else:
        if not lamp and not turn_ons[lucky]:
            lamp = True
            turn_ons[lucky] = True
    print('lucky=%d, lamp=%s, count=%d, %s' % (lucky, lamp, count, turn_ons))
    return lamp, count


solve_prisons(4)
