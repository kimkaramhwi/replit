def is_valid(string):
  stack=[]
  back_bracket_dict={')':'(', ']':'[', '}':'{'}
  for bracket in string:
    if bracket not in back_bracket_dict:
      stack.append(bracket)
    else:
      if stack :
        top=stack.pop()
      else:
          return False
      if back_bracket_dict[bracket] != top:
        return False
  if len(stack) != 0:
      return False
  return True

print(is_valid("(({}"))
print(is_valid('([{}])'))
print(is_valid('()[]{}'))