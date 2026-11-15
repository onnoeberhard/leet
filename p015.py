from bisect import bisect_left, bisect_right

def sol(nums):
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n - 2):
        x = nums[i]
        if x + nums[i + 1] + nums[i + 2] > 0: break
        if x + nums[n - 2] + nums[n - 1] < 0: continue
        if i > 0 and x == nums[i - 1]: continue
        j, k = i + 1, n - 1
        while j < k:
            y, z = nums[j], nums[k]
            s = x + y + z
            if s < 0: j += 1
            elif s > 0: k -= 1
            else:
                res.append((x, y, z))
                while j < k and nums[j] == y: j += 1
                while j < k and nums[k] == z: k -= 1
    return res

def sol2(nums):
    found = set()
    nums.sort()
    for i, x in enumerate(nums[:-2]):
        j = bisect_right(nums, -x - nums[-1], i + 2, len(nums) - 2) - 1
        for j, y in enumerate(nums[j:-1], j):
            k = bisect_left(nums, -x - y, j + 1, len(nums) - 1)
            if x + y + (z := nums[k]) == 0: found.add((x, y, z))
    return list(found)

