def top_k(nums, k):
    my_dict = {}
    
    for i in nums:
      if i not in my_dict:
        my_dict[i] = 1
      else:
        my_dict[i] += 1

    count_list = sorted(list(my_dict.values()), reverse=True)
    result = []

    for i in count_list[:k]:
    #   for key, value in my_dict.items():
    #     if i == value:
    #       result.append(key)
        max_number = [ key for key, value in my_dict.items() if value == i ]
        result += max_number

    if len(result) != k:
      return False
    return result

nums = [1,1,2,2,2,2,3,4,4,4]
k = 2
print(top_k(nums, k))