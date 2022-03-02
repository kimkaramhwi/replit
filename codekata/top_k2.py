def top_k(nums, k):
  set_nums = set(nums)
  result = [(target, nums.count(target)) for target in set_nums]
  result.sort(key = lambda x : -x[1])
  print(result)
  return [result[i][0] for i in range(k)]

nums = [1,2,2,2,3,3,3,4,4,4,4]
k = 2
print(top_k(nums, k))