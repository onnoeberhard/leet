def sol(s):
    num = ['0']
    sign = 1
    started = False
    for c in s:
        match c:
            case ' ' if not started: continue
            case '+' if not started: started = True
            case '-' if not started:
                sign = -1
                started = True
            case c if c in '0123456789':
                started = True
                num.append(c)
            case _: break

    max = 2**31 - 1 if sign == 1 else 2**31
    n = 0
    for i, d in enumerate(num[::-1]):
        n += (ord(d) - 48) * 10**i
        if n > max:
            n = max
            break

    return sign * n


def sol_old(s):  # not valid
    s = s.strip()
    sign = 1
    if s.startswith('-'):
        sign = -1
        s = s[1:]
    elif s.startswith('+'):
        s = s[1:]
    num = re.match('\d+', s)
    if num:
        num = sign * int(num.group(0))
        num = min(max(num, int(-2**31)), int(2**31)-1)
        return num
    return 0
