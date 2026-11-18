from math import inf

def sol(nums, target):
    nums.sort()
    res = None
    err = inf
    for i, x in enumerate(nums):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            s = x + nums[j] + nums[k]
            e = s - target
            if abs(e) < err: res, err = s, abs(e)
            if e < 0: j += 1
            elif e > 0: k -= 1
            else: return res
    return res
