# dir() : dir()내장 함수는 어떤 객체를 인자로 넣어주면 해당 객체가 어떤 변수와 메소드를 가지고 있는지 나열해줍니다.
# iterable 객체 : 반복 가능한 객체 (list, dict, set, str, bytes, tuple, range)
# iterator 객체 : 값을 차례대로 꺼낼 수 있는 객체

L = [1,2,3]
iterator_L = L.__iter__()
# print("dir iterator_L = ", end=""), print(dir(iterator_L))

# print(iterator_L.__next__()) # 1
# print(iterator_L.__next__()) # 2
# print(iterator_L.__next__()) # 3
# print(iterator_L.__next__()) # StopIteration

L1 = [1,2,3,4]
I = iter(L1)

while True:
    try:
        X = next(I)
    except StopIteration:
        break
    print(X**2, end=' ')
print()

D = {'a':1, 'b':2, 'c':3}
I2 = iter(D)

while True:
    try:
        key = next(I2)
    except StopIteration:
        break
    print(key, end=" ")