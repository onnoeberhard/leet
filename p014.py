def sol(strs):
    prefix = ""
    for i, c in enumerate(strs[0]):
        for s in strs[1:]:
            if len(s) <= i or s[i] != c: return prefix
        prefix += c
    return prefix
