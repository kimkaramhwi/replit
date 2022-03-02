def roman_to_num(s):
      # 여기에 코드를 작성해주세요.
  roman_num = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}

  try:
    s = list(s)
    sum = 0
    for i in range(len(s)):
      if roman_num[s[i]] >= roman_num[s[i+1]]:
        sum += roman_num[s[i]]
      else:
        sum -= roman_num[s[i]]
        
  except IndexError:
    sum += roman_num[s[i]]
  return sum

print(roman_to_num('MCMXCIV')) # 1994
print(roman_to_num('MMMDCXIV')) # 3614
print(roman_to_num('MMMDCXIX')) # 3619
print(roman_to_num('MMMCMXCIX')) # 3999