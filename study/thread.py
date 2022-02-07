import time
import threading

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

lock = threading.Lock()
shared_number = 0

def thread_1(number):
    lock.acquire()
    global shared_number
    print("number = ", end=""), print(number//2)
    for i in range(number//2):
        shared_number += 1
    lock.release()

def thread_2(number):
    lock.acquire()
    global shared_number
    print("number = ", end=""), print(number//2)
    for i in range(number//2, number):
        shared_number += 1
    lock.release()

if __name__ == "__main__":
    threads = []

    start_time = time.time()
    t1 = threading.Thread(target=thread_1, args=(10000000,))
    t1.start()
    threads.append(t1)

    t2 = threading.Thread(target=thread_2, args=(10000000,))
    t2.start()
    threads.append(t2)

    for t in threads:
        t.join()

    print("--- %s seconds ---" % (time.time() - start_time))
    print("shared_number=", end=""), print(shared_number)
    print("end of main")