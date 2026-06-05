from bisect import bisect_left

def two_sum(nums, target):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums[i + 1:], i + 1):
            if x + y == target: return i, j

def two_sum2(nums, target):
    perm = sorted(range(len(nums)), key=lambda i: nums[i])
    nums = [nums[i] for i in perm]
    for i, x in enumerate(nums):
        j = bisect_left(nums, target - x, i + 1)
        if x + nums[j] == target: break
    return perm.index(i), perm.index(j)  # type: ignore

def two_sum3(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        y = target - x
        if y in seen: return i, seen[y]
        seen[x] = i

