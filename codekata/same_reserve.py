def same_reverse(num):
    # 아래 코드를 입력해주세요.
    if num > 0:
      if int(str(num)[::-1]) == num:
        return True
      else:
        return False
    else:
      return False

print(same_reverse(101))