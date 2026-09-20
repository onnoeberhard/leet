from bisect import bisect_left, bisect_right

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

def sol_old(nums, target):
    def idx(l, r):
        a = nums.index(nums_[l])
        b = nums.index(nums_[r])
        if a == b:
            b = nums.index(nums_[r], a + 1)
        return [a, b]
    nums_ = sorted(nums)
    l = 0
    r = bisect_right(nums_, target - nums_[0])
    if r == len(nums):
        r -= 1
#            return [nums.index(nums_[0]), nums.index(nums_[-1])]
    while l != r:
        s = nums_[l] + nums_[r]
        if s == target:
            return idx(l, r)
#                return [nums.index(nums_[l]), nums.index(nums_[r])]
        elif s < target:
            l += 1
        else:
            r -= 1

