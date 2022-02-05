# ax = b
# 결과 출력물은 다음과 같아야 합니다.

# Input 으로 주어진 a 와 b 값으로 위의 방정식을 충족하는 단 하나의 정수가 존재한다면 해당 정수를 출력하면 됩니다
# 만일 a 와 b 값으로 위의 방정식을 충족하는 정수가 없다면 "No Solution"을 출력해주세요.
# a 와 b 값으로 위의 방정식을 충족하는 정수가 많다면 "Many Solutions"을 출력해주세요.
# Hint:

# a 나 b 는 0이 될 수 있습니다.
# Examples:

# 만일 a = 1, b = -2 라면 결과값으로 -2가 출력이 되어야 합니다.
# 만일 a = 2, b = -1 라면 결과값으로 "No Solution"이 출력이 되어야 합니다.

a = int(input('첫번째 정수'))
b = int(input('두번째 정수'))

if a == 0:
    if b != 0:
        print("No Solution")
    else:
        print("Many Solutions")
elif b%a == 0:
    print(b//a)
else:
    print("No Solution")
