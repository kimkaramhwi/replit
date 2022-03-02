def roman_to_num(s):
  # 여기에 코드를 작성해주세요.
  roman_num = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
  num = s[0]
  number = roman_num[num]

  for i in range(1,len(s)):
    bnum = num
    num = s[i]
    if roman_num[bnum]>=roman_num[num]:
      number += roman_num[num]
    else:
      number += roman_num[num] - 2*roman_num[bnum]

  return number

print(roman_to_num('CMLIV')) 
