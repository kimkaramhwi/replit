def move_zeroes(nums):
    for i in reversed(range(len(nums))):
        if nums[i] == 0:
            del nums[i]
            nums.append(0)

    return nums

nums = [0,0,9,0,12]
print(move_zeroes(nums))