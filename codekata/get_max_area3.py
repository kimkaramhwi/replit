def get_max_area(height):
  max_area=0
  for index1 in range(len(height)):
    for index2 in range(index1,len(height)):
      current_area=(index2-index1)*min(height[index2],height[index1])
      max_area=max(max_area,current_area)
      
  return  max_area

height = [11, 80, 60, 20, 50, 100, 100, 3, 10]
print(get_max_area(height))