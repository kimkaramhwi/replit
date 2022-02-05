# find_smallest_integer_divisor 함수는 하나의 parameter를 받습니다.
# Parameter 값은 integer만 주어집니다.
# find_smallest_integer_divisor 주어진 parameter 값을 나눌 수 있는 1을 제외한 최소의 양의 정수를 return하여야 합니다.
# find_smallest_integer_divisor(15) == 3

def find_smallest_integer_divisor(num):
    i = 2

    while num % i != 0:
        i += 1
    else:
        return i

print(find_smallest_integer_divisor(15))