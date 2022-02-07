# from multiprocessing import Process, Queue
# import time

# def worker(id, number, q):
#     increased_number = 0

#     for i in range(number):
#         increased_number += 1

#     q.put(increased_number)
#     return

# if __name__ == "__main__":
#     start_time = time.time()
#     q = Queue()

#     th1 = Process(target=worker, args=(1, 50000000, q))
#     th2 = Process(target=worker, args=(2, 50000000, q))

#     th1.start()
#     th2.start()
#     th1.join()
#     th2.join()

#     print("---%s seconds ---" % (time.time() - start_time))
#     q.put('exit')

#     total = 0
#     while True:
#         tmp = q.get()
#         if tmp == 'exit':
#             break
#         else:
#             total += tmp

#     print("total_number=", end=""), print(total)
#     print("end of main")

from multiprocessing import Process, shared_memory, Semaphore
import numpy as np

def func(id, number, new_array, shm, sem):
    increased_number = 0
    for i in range(number):
        increased_number += 1
    sem.acquire()
    ex_shm = shared_memory.SharedMemory(name=shm)
    b = np.ndarray(new_array.shape, dtype=new_array.dtype, buffer=ex_shm.buf)
    b[0] += increased_number
    sem.release()

if __name__ == "__main__":
    sem = Semaphore(1)
    new_array = np.array([0])
    shm = shared_memory.SharedMemory(create=True, size=new_array.nbytes)
    c = np.ndarray(new_array.shape, dtype=new_array.dtype, buffer=shm.buf)

    th1 = Process(target=func, args=(1, 50000000, new_array, shm.name, sem))
    th2 = Process(target=func, args=(2, 50000000, new_array, shm.name, sem))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print("total_number=", end=""), print(c[0])
    print("end of main")
    shm.close()
    shm.unlink()