
import math

def guess_name():
    names = '赵钱孙李周吴郑王冯程储卫蒋武韩'
    lines = get_lines(names)
    while True:
        answers = []
        for line in lines:
            print(', '.join(line))
            answer = input('Is your name in this line?(y/n)')
            answer = 1 if answer in ('y', 'Y') else 0
            answers.append(answer)
        name = get_name(answers, names)
        print('Your name is:', name)
        answer = input('Continue?(y/n)')
        if answer not in ('y', 'Y'):
            break


def get_lines(names):
    rows = int(math.log2(len(names))) + 1
    lines = [[] for _ in range(rows)]
    for i, name in enumerate(names):
        id = i + 1
        for j in range(rows):
            if id % 2 == 1:
                lines[j].append(name)
            id //= 2
    return lines



def get_name(answers, names):
    id = 0
    for digit in reversed(answers):
        id = id * 2 + digit
    return '不存在的姓' if id == 0 else names[id - 1]


guess_name()