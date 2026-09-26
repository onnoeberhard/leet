def sol(s):
    l, lo, hi = 0, 0, 0
    for i in range(len(s)):
        # Odd palindromes
        j = 0
        while j < min(i, len(s) - i - 1):
            if s[i - j - 1] != s[i + j + 1]: break
            j += 1
        l_ = 2 * j + 1
        if l_ > l: l, lo, hi = l_, i - j, i + j + 1

        # Even palindromes
        j = 0
        while j < min(i + 1, len(s) - i - 1):
            if s[i - j] != s[i + j + 1]: break
            j += 1
        l_ = 2 * j
        if l_ > l: l, lo, hi = l_, i - j + 1, i + j + 1

    return s[lo:hi]

def sol2(s):
    def f(i, stack, p):
        # possible improvement: instead of real stack, use indices.
        l, t = 0, ''
        if i != len(s) and not p:  # Push possible
            l_, t_ = f(i + 1, stack + (s[i],), False)
            l, t = (l_, t_) if l_ > l else (l, t)
        if i != len(s) and stack and s[i] == stack[-1]:  # Pop possible
            l_, t_ = f(i + 1, stack[:-1], True)
            l_, t_ = 2 + l_, s[i] + t_
            l, t = (l_, t_) if l_ > l else (l, t)
        if stack and not p:  # Pop first possible
            l_, t_ = f(i, stack[:-1], True)
            l_, t_ = 1 + l_, stack[-1] + t_
            l, t = (l_, t_) if l_ > l else (l, t)
        return l, t

    l, s = f(0, (), False)
    return s[::-1] + s if l % 2 == 0 else s[:0:-1] + s


