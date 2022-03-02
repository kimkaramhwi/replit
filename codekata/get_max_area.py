def get_max_area(height):
  start = 0
  last = len(height)-1
  max_area = 0

  for i in range(len(height)-1):
    max_area = max(max_area, min(height[start], height[last])*(last-start))
    if height[start] > height[last]:
      last -= 1
    else:
      start += 1

  return max_area

height =  [1, 8, 25, 2, 25, 4, 8, 3, 7]
print(get_max_area(height))