from math import ceil, floor, inf

def sol(a, b):
    if len(a) > len(b): a, b = b, a
    lo, hi = 0, len(a)
    half = (len(a) + len(b) + 1) // 2

    while lo <= hi:
        i = (hi + lo) // 2
        j = half - i
        
        al = a[i - 1] if i > 0 else -inf
        ar = a[i] if i < len(a) else inf
        bl = b[j - 1] if j > 0 else -inf
        br = b[j] if j < len(b) else inf
        
        if al <= br and bl <= ar:
            return max(al, bl) if (len(a) + len(b)) % 2 == 1 \
                else (max(al, bl) + min(ar, br)) / 2

        if al > br: hi = i - 1
        else: lo = i + 1

def sol2(a, b):
    lo1 = floor(max((len(a) - 1)/2 - len(b), 0))
    hi1 = max(lo1, ceil(min((len(a) - 1)/2 + len(b), len(a) - 1)))
    lo2 = floor(max((len(b) - 1)/2 - len(a), 0))
    hi2 = max(lo2, ceil(min((len(b) - 1)/2 + len(a), len(b) - 1)))
    i = (lo1 + hi1) / 2
    j = (lo2 + hi2) / 2

    while lo1 < hi1 and lo2 < hi2:
        if a[ceil(i)] < b[floor(j)]:
            lo1 = ceil(i)
            hi2 = floor(j)
            d = max(hi1 - lo1, hi2 - lo2) / 2
            d = min(max(d, lo1 - i, j - hi2), hi1 - i, j - lo2)
            i += d
            j -= d
        elif b[ceil(j)] < a[floor(i)]:
            hi1 = floor(i)
            lo2 = ceil(j)
            d = max(hi1 - lo1, hi2 - lo2) / 2
            d = min(max(d, i - hi1, lo2 - j), i - lo1, hi2 - j)
            i -= d
            j += d
        else: break

    # Push indices out of bounds if appropriate
    if not (lo1 == hi1 and lo2 == hi2) and len(a) and len(b):
        if lo1 == hi1 and a[int(i)] < b[floor(j - 1/2)] or lo2 == hi2 \
            and b[int(j)] > a[ceil(i + 1/2)]: i, j = i + 1/2, j - 1/2
        elif lo1 == hi1 and a[int(i)] > b[ceil(j + 1/2)] or lo2 == hi2 \
            and b[int(j)] < a[floor(i - 1/2)]: i, j = i - 1/2, j + 1/2
            
    nums = sorted(
        ([a[i] for i in {floor(i), ceil(i)}] if 0 <= i <= len(a) - 1 else []) +
        ([b[j] for j in {floor(j), ceil(j)}] if 0 <= j <= len(b) - 1 else []))
    mid = (len(nums) - 1) / 2
    return (nums[floor(mid)] + nums[ceil(mid)]) / 2

