def sol(digits):
    abc = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    keys = {str(x): a for x, a in zip(range(2, 10), abc)}
    res = []
    for d in digits:
        res = [t + c for t in res for c in keys[d]]
    return res


def sol_old(digits):
    from math import prod
    if not digits:
        return []
    x = []
    pad = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    letters = [pad[int(d) - 2] for d in digits]
    lens = [len(ls) for ls in letters]
    for i in range(prod(lens)):
        idx = [i // prod(lens[j+1:]) % ls for j, ls in enumerate(lens)]
        x.append(''.join(letters[j][idx[j]] for j in range(len(digits))))
    return x
