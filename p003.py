def sol(s):
    res = 0
    sub = {}
    for i, c in enumerate(s):
        if c in sub:
            res = max(res, len(sub))
            sub = {k: j for j, k in enumerate(s[sub[c] + 1 : i], sub[c] + 1)}
        sub[c] = i
    return max(res, len(sub))

def sol2(s):
    if s == "": return 0
    res = 0
    seen = {}
    lo = i = 0
    for i, c in enumerate(s):
        if c in seen and seen[c] >= lo:
            res = max(res, i - lo)
            lo = seen[c] + 1
        seen[c] = i
    return max(res, i - lo + 1)

def sol_old(s):
    lng = 0
    cur = ""
    for c in s:
        if c in cur:
            cur = cur[cur.index(c) + 1:]
        cur += c
        if len(cur) > lng:
                lng = len(cur)
    return lng

