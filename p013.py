def sol(s):
    d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    x = 0
    y_ = 0  # number to the right of y
    for c in s[::-1]:
        y = d[c]
        sign = -1 if y_ > y else 1
        x += sign * y
        y_ = y
    return x

def sol_old(s):
    nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r = 0
    for i, n in enumerate(s):
        if i < len(s) - 1 and nums[n] < nums[s[i + 1]]:
            r -= nums[n]
        else:
            r += nums[n]
    return r

