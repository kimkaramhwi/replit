# 파이썬에서 보통의 함수는 값을 반환하고 종료 하지만 제너레이터 함수는 값을 반환하기는 하지만 산출(yield)한다.
# 이터레이터를 생성해주는 함수

# def generator_send():
#     received_value = 0

#     while True:
#         received_value = yield
#         print("received_value = ", end=""), print(received_value)
#         yield received_value * 2

# gen = generator_send()
# next(gen)
# print(gen.send(2))

# next(gen)
# print(gen.send(3))

L = [1,2,3]

# def generate_square_from_list():
#     result = (x*x for x in L)
#     print(result)
#     return result

# def print_iter(iter):
#     for element in iter:
#         print(element)

# print_iter(generate_square_from_list())

from ast import comprehension
import time

def print_iter(iter):
    for element in iter:
        print(element)

def lazy_return(num):
    print("sleep 1s")
    time.sleep(1)
    return num

print("comprehension_list=")
comprehension_list = [lazy_return(i) for i in L]
print_iter(comprehension_list)

print("generator_exp=")
generator_exp = (lazy_return(i) for i in L)
print_iter(generator_exp)