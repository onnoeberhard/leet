def sol(s, n):
    l = [""] * n
    i = 0
    d = 1  # direction: down (1) or up (-1)
    for c in s:
        l[i] += c
        if n == 1: continue
        if d == 1 and (i + 1) % n == 0 or d == -1 and i == 0:
            d *= -1
        i += d
    return ''.join(l)

