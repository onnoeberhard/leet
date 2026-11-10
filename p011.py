def sol(height):
    i = 0
    j = len(height) - 1
    h = min(height[i], height[j])
    d = j - i
    while i < j:
        if height[i] <= h: i += 1
        elif height[j] <= h: j -= 1
        elif min(height[i], height[j]) * (j - i) > h * d:
            h = min(height[i], height[j])
            d = j - i
        elif height[i] < height[j]: i += 1
        else: j -= 1

    return h * d

