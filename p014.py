def sol(strs):
    prefix = ""
    for i, c in enumerate(strs[0]):
        for s in strs[1:]:
            if len(s) <= i or s[i] != c: return prefix
        prefix += c
    return prefix

def sol_old(strs):
    prefix = ""
    i = 0
    while True:
        if len(strs[0]) == i:
            break
        c = strs[0][i]
        for j in range(1, len(strs)):
            if len(strs[j]) == i or strs[j][i] != c:
                return prefix
        prefix += c
        i += 1
    return prefix
