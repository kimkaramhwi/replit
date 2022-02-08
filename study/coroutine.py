import time

# def coroutine_test():
#     greeting = "good"
#     while True:
#         text = (yield greeting)
#         print("text= ", end= ""), print(text)
#         greeting += text

# if __name__ == "__main__":
#     cr = coroutine_test()
#     print("cr=", end=""), print(cr)

#     next(cr) # 코루틴 최초 실행 'good' 저장
#     time.sleep(2)

#     print("send 1")
#     print(cr.send("morning")) # 마지막으로 저장된 'good'뒤에서 실행을 재개
#     time.sleep(2)

#     print("send 2")
#     print(cr.send("afternoon"))
#     time.sleep(2)

#     print("send 3")
#     print(cr.send("evening"))
#     time.sleep(2)


# def number_coroutine():
#     while True:        # 코루틴을 계속 유지하기 위해 무한 루프 사용
#         x = (yield)    # 코루틴 바깥에서 값을 받아옴, yield를 괄호로 묶어야 함
#         print(x)
 
# co = number_coroutine()
# co.send(None)      # 코루틴 안의 yield까지 코드 실행(최초 실행)
 
# co.send(1)    # 코루틴에 숫자 1을 보냄
# co.send(2)    # 코루틴에 숫자 2을 보냄
# co.send(3)    # 코루틴에 숫자 3을 보냄


# def coroutine_1():
#     return_value = 0
#     while True:
#         input_value = (yield return_value)
#         return_value = input_value + 1

# def coroutine_2():
#     return_value = 0
#     while True:
#         input_value = (yield return_value)
#         return_value = input_value + 1

# if __name__ == "__main__":
#     ret_value = 0

#     c1 = coroutine_1()
#     c2 = coroutine_2()

#     next(c1)
#     next(c2)

#     while ret_value < 100000000:
#         ret_value = c1.send(ret_value)
#         ret_value = c2.send(ret_value)

#     print("ret_value =", end=""), print(ret_value)
#     print("end of main")



# def coroutine_test():
#     greeting = "good"
#     while True:
#         # text = (yield greeting)
#         # print(greeting + text)
#         text = (yield greeting)
#         print("text = ", end=""), print(text)
#         greeting = "good"
#         greeting += text

# if __name__ == "__main__":
#     cr = coroutine_test()
#     print("cr=", end=""), print(cr)

#     next(cr)
#     time.sleep(2)

#     print("send 1")
#     print(cr.send("morning"))
#     time.sleep(2)

#     print("send 2")
#     print(cr.send("afternoon"))
#     time.sleep(2)

#     print("send 3")
#     print(cr.send("evening"))
#     time.sleep(2)


# def number_coroutine():
#     try:
#         while True:
#             x = (yield)
#             print(x, end=' ')
#     except GeneratorExit:    # 코루틴이 종료 될 때 GeneratorExit 예외 발생
#         print()
#         print('코루틴 종료')
 
# co = number_coroutine()
# next(co)
 
# for i in range(20):
#     co.send(i)
 
# co.close()



# def sum_coroutine():
#     try:
#         total = 0
#         while True:
#             x = (yield)
#             total += x
#     except RuntimeError as e:
#         print(e)
#         yield total    # 코루틴 바깥으로 값 전달
 
# co = sum_coroutine()
# next(co)
 
# for i in range(20):
#     co.send(i)
 
# print(co.throw(RuntimeError, '예외로 코루틴 끝내기'))


# import asyncio
 
# async def hello():    # async def로 네이티브 코루틴을 만듦
#     print('Hello, world!')
 
# loop = asyncio.get_event_loop()     # 이벤트 루프를 얻음
# loop.run_until_complete(hello())    # hello가 끝날 때까지 기다림
# loop.close()                        # 이벤트 루프를 닫음


import asyncio

async def coroutine_1(num):
    result_value = 0
    while result_value < num:
        result_value += 1
    return result_value

async def coroutine_2(num):
    result_value = 0
    while result_value < num:
        result_value += 1
    return result_value

async def main():
    one = await coroutine_1(50000000)
    two = await coroutine_2(50000000)
    # await asyncio.sleep(1.0)
    print("ret_value=", end="")
    print(one+two)
    print("end of main")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()