def sol(nums, target):
    nums.sort()
    res = set()
    for i in range(len(nums)):
        if 0 <= target < nums[i]: break
        xs = sum3(nums, i + 1, target - nums[i])
        for x in xs: res.add((nums[i], *x))
    return list(res)

def sum3(nums, lo, target):
    res = []
    for i in range(lo, len(nums)):
        if 0 <= target < nums[i]: break
        j, k = i + 1, len(nums) - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum == target: res.append((nums[i], nums[j], nums[k]))
            if sum <= target: j += 1
            else: k -= 1
    return res

