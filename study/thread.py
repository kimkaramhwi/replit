import time
import threading


# class Worker(threading.Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name            # thread 이름 지정

#     def run(self):
#         print("sub thread start ", threading.current_thread().getName())
#         time.sleep(3)
#         print("sub thread end ", threading.current_thread().getName())


# print("main thread start")
# for i in range(5):
#     name = "thread {}".format(i)
#     t = Worker(name)                # sub thread 생성
#     t.start()                       # sub thread의 run 메서드를 호출

# print("main thread end")


# class Worker(threading.Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name            # thread 이름 지정

#     def run(self):
#         print("sub thread start ", threading.currentThread().getName())
#         time.sleep(3)
#         print("sub thread end ", threading.currentThread().getName())


# print("main thread start")
# for i in range(5):
#     name = "thread {}".format(i)
#     t = Worker(name)                # sub thread 생성
#     t.daemon = True
#     t.start()                       # sub thread의 run 메서드를 호출

# print("main thread end")


# class Worker(threading.Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name            # thread 이름 지정

#     def run(self):
#         print("sub thread start ", threading.currentThread().getName())
#         time.sleep(5)
#         print("sub thread end ", threading.currentThread().getName())


# print("main thread start")

# t1 = Worker("1")        # sub thread 생성
# t1.start()              # sub thread의 run 메서드를 호출

# t2 = Worker("2")        # sub thread 생성
# t2.start()              # sub thread의 run 메서드를 호출

# t1.join()
# t2.join()

# print("main thread post job")
# print("main thread end")


# class Worker(threading.Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name            # thread 이름 지정

#     def run(self):
#         print("sub thread start ", threading.currentThread().getName())
#         time.sleep(5)
#         print("sub thread end ", threading.currentThread().getName())


# print("main thread start")

# threads = []
# for i in range(3):
#     thread = Worker(i)
#     thread.start()              # sub thread의 run 메서드를 호출
#     threads.append(thread)


# for thread in threads:
#     thread.join()

# print("main thread post job")
# print("main thread end")


# if __name__ == "__main__":

#     increased_num = 0

#     start_time = time.time()
#     for i in range(100000000):
#         increased_num += 1

#     print("--- %s seconds ---" % (time.time() - start_time))
#     print("increased_num=", end=""), print(increased_num)
#     print("end of main")



# shared_number = 0
# def thread_1(number):
#     global shared_number
#     print("number = ", end=""), print(number)

#     for i in range(number):
#         shared_number += 1

# def thread_2(number):
#     global shared_number
#     print("number = ", end=""), print(number)
#     for i in range(number):
#         shared_number += 1

# if __name__ == "__main__":
#     threads = [ ]

#     start_time = time.time()
#     t1 = threading.Thread(target=thread_1, args=(5000000,))
#     t1.start()
#     threads.append(t1)

#     t2 = threading.Thread(target=thread_2, args=(5000000,))
#     t2.start()
#     threads.append(t2)

#     for t in threads:
#         t.join()

#     print("---%s seconds ---" % (time.time() - start_time))
#     print("shared_number=", end=""), print(shared_number)
#     print("end of main")



shared_number = 0
lock = threading.Lock()

def thread_1(number):
    global shared_number
    print("number = {}".format(number))
    
    for i in range(number):
        lock.acquire()
        shared_number += 1
        lock.release()

def thread_2(number):
    global shared_number
    print("number = {}".format(number))
    for i in range(number):
        lock.acquire()
        shared_number += 1
        lock.release()


if __name__ == "__main__":

    threads = [ ]

    start_time = time.time()
    t1 = threading.Thread( target= thread_1, args=(50000000,) )
    t1.start()
    threads.append(t1)

    t2 = threading.Thread( target= thread_2, args=(50000000,) )
    t2.start()
    threads.append(t2)


    for t in threads:
        t.join()

    print("--- %s seconds ---" % (time.time() - start_time))

    print("shared_number=",end=""), print(shared_number)
    print("end of main")



# t1_number = 0
# t2_number = 0

# def thread_1(number):
#     global t1_number
#     print("number = {}".format(number))
    
#     for i in range(number):
#         t1_number += 1

# def thread_2(number):
#     global t2_number
#     print("number = {}".format(number))
#     for i in range(number):
#         t2_number += 1


# if __name__ == "__main__":

#     threads = [ ]

#     start_time = time.time()
#     t1 = threading.Thread( target= thread_1, args=(50000000,) )
#     t1.start()
#     threads.append(t1)

#     t2 = threading.Thread( target= thread_2, args=(50000000,) )
#     t2.start()
#     threads.append(t2)


#     for t in threads:
#         t.join()

#     print("--- %s seconds ---" % (time.time() - start_time))

#     print("result number = {}".format(t1_number + t2_number))
#     print("end of main")