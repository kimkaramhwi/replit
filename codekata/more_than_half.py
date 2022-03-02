def more_than_half(nums):
  # 아래 코드를 입력해주세요.
  number = {}

  for i in nums:
    if i not in number:
      number[i] = 1
    else:
      number[i] += 1
  
  max_value = max(number.values())

  for key, value in number.items():
    if value == max_value:
      return key

nums = [1,1,1,1,2,2,2,2,2,2,2,2,2,2,1,1]
print(more_than_half(nums))