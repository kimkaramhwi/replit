def more_than_half(nums):
    # 아래 코드를 입력해주세요.
    print(len(nums))
    half = len(nums) / 2
    params = set(nums)
    for i in params:
      if nums.count(i) > half:
        return i

nums = [1,1,1,1,2,2,2,2,2,2,2,2,2,2,1,1,3,3,3,3,3,3]
print(more_than_half(nums))