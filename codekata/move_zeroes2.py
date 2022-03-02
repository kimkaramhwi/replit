def move_zeroes(nums):
  last0 = 0
  
  for i in range(len(nums)):
    if nums[i] != 0:
      nums[i], nums[last0] = nums[last0], nums[i]
      last0 += 1
      
  return nums
nums = [0,0,9,0,12]
print(move_zeroes(nums))