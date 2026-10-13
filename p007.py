def sol(x):
    sign = -1 if x < 0 else 1
    x = str(abs(x))[::-1]
    hi = str(2**31 - 1 if sign > 0 else 2**31)
    if len(x) > len(hi): return 0
    x = f'{x:0>{len(hi)}}'
    for c, m in zip(x, hi):
        if c < m: break
        if c > m: return 0
    return sign * int(x)

def sol_old(x):  # not technically valid.
    if x < 0:
        x = -int(str(x)[:0:-1])
        if x >= -2**31:
            return x
    else:
        x = int(str(x)[::-1])
        if x <= 2**31 - 1:
            return x
    return 0

