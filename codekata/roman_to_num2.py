def roman_to_num(s):
  # 여기에 코드를 작성해주세요.
  roman_num = ["M", "D", "C", "L", "X", "V", "I"]
  roman_num_value = [1000, 500, 100, 50, 10, 5, 1]
  exception = ["IV", "IX", "XL", "XC", "CD", "CM"]
  exception_value = [4, 9, 40, 90, 400, 900]
  result = 0

  for i in range(len(exception)):
    if exception[i] in s:
      s = s.replace(exception[i], '')
      result += exception_value[i]


  for k in range(len(roman_num)):
    while roman_num[k] in s:
      s = s[1:]
      result += roman_num_value[k]

  return result


print(roman_to_num('MCMXCIV')) # 1994
print(roman_to_num('MMMDCXIV')) # 3614
print(roman_to_num('MMMDCXIX')) # 3619
print(roman_to_num('MMMCMXCIX')) # 3999
