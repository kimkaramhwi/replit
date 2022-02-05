# 함수 sum_of_numbers는 argument로 주어지는 모든 수를 합한 값을 return 해야 합니다.
# what_is_my_full_name 함수는 주어진 parameter중 first_name 과 last_name 이라는 parameter를 조합하여 full name을 return 해주어야 합니다.
# 예를 들어, first_name이 "우성" 이고 last_name 이 "정" 이면 "정 우성" 라고 return 하면 됩니다.
# Last name과 first name 사이에 space(빈칸)이 들어가 있어야 합니다.
# 만일 last_name이 없거나 first_name이 없으면 둘 중하나만 return 하면 됩니다.

def sum_of_numbers(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

def what_is_my_full_name(**kwargs):
    if "last_name" in kwargs and "first_name" in kwargs:
        return f'{kwargs["last_name"]} {kwargs["first_name"]}'
    elif "last_name" in kwargs and "first_name" not in kwargs:
        return f'{kwargs["last_name"]}'
    elif "last_name" not in kwargs and "first_name" in kwargs:
        return f'{kwargs["first_name"]}'
    else:
        return "Nobody"

print(sum_of_numbers(1,2,3,4,5))
print(what_is_my_full_name(first_name="우성", last_name="정"))