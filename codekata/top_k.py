def top_k(nums, k):
    max_val = []
    result  = []
    number  = set(nums)

    for i in number:
        max_val.append(nums.count(i))

    max_val = sorted(max_val, reverse=True)

    for j in range(k):
        for n in number:
            if nums.count(n) == max_val[j]:
                result.append(n)
    
    if len(result) != k:
        return False

    result.sort()
    return result
    
nums = [1,2,2,2,3,3,3,1,1,1,4,4,4,4,4]
print(top_k(nums, 2))