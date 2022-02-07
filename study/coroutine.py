# import time

# def coroutine_test():
#     greeting = "good"
#     while True:
#         text = (yield greeting)
#         print("text= ", end= ""), print(text)
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
#         text = (yield greeting)
#         print(greeting + text)

# if __name__ == "__main__":
#     cr = coroutine_test()
#     print("cr=", end=""), print(cr)

#     next(cr)
#     time.sleep(2)

#     print("send 1")
#     cr.send("morning")
#     time.sleep(2)

#     print("send 2")
#     cr.send("afternoon")
#     time.sleep(2)

#     print("send 3")
#     cr.send("evening")
#     time.sleep(2)



import asyncio

async def coroutine(num):
    result_value = 0
    while result_value < num:
        result_value += 1
    return result_value

async def main():
    one = await coroutine(50000000)
    two = await coroutine(50000000)
    print("ret_value=", end="")
    print(one+two)
    print("end of main")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()