from operator import indexOf


# def two_sum(nums, target):
#     for i in nums[:-1]:
#         for j in nums[1:]:
#             if i + j == target:
#                 return indexOf(nums, i), indexOf(nums, j)

def two_sum(nums, target):
    my_list = []
    length = len(nums)
    for i in range(length-1):
        for j in range(1, length):
            if nums[i] + nums[j] == target:
                my_list.append(i)
                my_list.append(j)
                return my_list

nums = [4,9,11,14,15]
target = 29
print(two_sum(nums, target))