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

def sol_old(self, s):
    rs = [i for i in range(len(s) - 1) if s[i] == s[i + 1]]
    cs = list(range(len(s)))
    longest = s[rs[0] : rs[0] + 2] if rs else s[cs[0]]
    
    for l in range(1, len(s)):
        cs_ = []
        for c in cs:
            if c - l >= 0 and c + l < len(s) and s[c - l] == s[c + l]:
                cs_.append(c)
        
        rs_ = []
        for r in rs:
            if r - l >= 0 and r + l + 1 < len(s) and s[r - l] == s[r + l + 1]:
                rs_.append(r)
                
        if rs_ or cs_:
            rs = rs_
            cs = cs_
            longest = s[rs[0] - l : rs[0] + l + 2] if rs else s[cs[0] - l : cs[0] + l + 1]
        else:
            break
    
    return longest

