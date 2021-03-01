
def queens(num:int, idx:int=0, dist:list=None):
    if idx == num:
        return True
    if dist is None:
        dist = []

    for col in range(num):
        if available(idx, col, dist):
            dist.append(col)
            if queens(num, idx+1, dist):
                return True
            del dist[-1]
    return False


def available(row, col, dist):
    for i_row, i_col in enumerate(dist):
        if col == i_col or row - i_row == col - i_col or row - i_row == i_col - col:
            return False
    return True


dist = []
num = input('number of the queens is: ')
num = int(num)
if queens(num, dist=dist):
    for col in dist:
        print('- ' * col, end='')
        print('Q ', end='')
        print('- ' * (num - col - 1))
else:
    print('no solution!')



exec()