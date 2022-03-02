def get_len_of_str(s):
    # 아래 코드를 작성해주세요.
  new_list = []
  result = []

  for i in s:
    if i not in new_list:
      new_list.append(i)
    else:
      result.append(len(new_list))
      new_list = []
      new_list.append(i)

  result.append(len(new_list))
  return max(result)

print(get_len_of_str("sttrg"))