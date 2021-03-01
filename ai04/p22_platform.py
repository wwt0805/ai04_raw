
import p21_Exp as exp


def solve(exps, lr=0.001, epoches=10000):
    vars = set()
    derivs = {e: {v: e.deriv(v) for v in e.get_vars()} for e in exps}

    for e in derivs:
        for v in derivs[e]:
            vars.add(v)
    vars = {v:1.0 for v in vars}

    for _ in range(epoches):
        for e in exps:
            vs = derivs[e]
            ds = {}
            for v in vs:
                deriv = vs[v]
                delta = -lr * deriv.eval(env=vars)
                ds[v] = delta
            for v in vs:
                vars[v] = vars[v] + ds[v]

    return vars


def main():
    v = [exp.Variable(chr(ord('a') + i)) for i in range(26)]
    exps = []
    while True:
        s = input('expression = ?')
        if len(s) == 0:
            break
        s = eval(s)
        exps.append(s)
    print(solve(exps))


if __name__ == '__main__':
    main()
    # x = exp.Variable('x')
    # y = exp.Variable('y')
    # exps = []
    # s = (3 * x - 4 * y) ** 2
    # exps.append(s)
    # s = (2 * x + 3 * y - 4) ** 2
    # exps.append(s)
    #
    # print(solve(exps))


