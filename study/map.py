# my_list = [1, 2, 3, 4, 5]

# # for 반복문 이용
# result1 = []
# for val in my_list:
#     result1.append(val+1)

# print(f'result1 : {result1}')

# # map 함수 이용
# def add_one(n):
#     return n+1

# result2 = list(map(add_one, my_list))
# print(f'result2 : {result2}')

# print(list(map(int, ['1','2','3',4.5, 5.8])))

# ten_times1 = map(lambda x: 10*x, (1, 2, 3, 4, 5))
# ten_times2 = map(lambda x: 10*x, range(1, 6))

# # ten_times1[0]
# print(list(ten_times1)[0])

print(list(map(lambda x, y : x + y, [1, 2, 3], (9, 13, 2))))

def elewise_mul(x,y,z):
    return x*y*z

print(list(map(elewise_mul, [1, 2, 3], [1, 3, 5], [2, 4, 6])))