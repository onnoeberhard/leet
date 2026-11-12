def sol(num):
    ns = [1000, 500, 100, 50, 10, 5, 1]
    cs = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    s = ''
    for i, (n, c) in enumerate(zip(ns, cs)):
        if i % 2 == 1 and num // ns[i + 1] == 9:
            s += cs[i + 1] + cs[i - 1]
            num %= ns[i + 1]
            continue
        m, num = divmod(num, n)
        if m == 4: s += c + cs[i - 1]
        else: s += m * c
    return s
