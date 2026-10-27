def sol(s, p):
    i = j = 0
    fallback = []
    star = False
    while j < len(p):
        if j + 1 < len(p) and p[j + 1] == '*':
            star = True
            fallback.append((i, j + 2))
        if i < len(s) and (s[i] == p[j] or p[j] == '.'):
            i += 1
            j += not star
        elif fallback:
            i, j = fallback.pop()
            star = False
        else: return False
    return i == len(s)

