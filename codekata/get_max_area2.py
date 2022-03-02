def get_max_area(height):
    start = 0
    last = len(height)-1
    area = 0

    while start < last:
        area = max(area, min(height[start], height[last])*(last-start))
        if height[start] > height[last]:
            last -= 1
        else:
            start += 1
    return area

height = [1, 8, 25, 2, 25, 4, 8, 3, 7]
print(get_max_area(height))