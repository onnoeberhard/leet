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

def sol_old(self, nums):
    r = []
    if len(nums) == 0:
        return r
    nums.sort()
    tried1 = tried2 = nums[0] - 1
    for i in range(len(nums) - 2):
        if nums[i] > 0:
            return r
        if nums[i] == tried1:
            continue
        tried1 = nums[i]
        # Two-sum for -nums[i]
        for j in range(i + 1, len(nums) - 1):
            if nums[j] == tried2:
                continue
            tried2 = nums[j]
            if nums[i] + nums[j] > 0:
                break
            # Binary search for third number
            y = -(nums[i] + nums[j])
            k = bisect_left(nums, y, j + 1)
            if k != len(nums) and nums[k] == y and (x := [nums[i], nums[j], nums[k]]) not in r:
                r.append(x)
    return r
