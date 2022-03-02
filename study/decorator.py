# z = 3

# def outer(x):
#     y = 10
#     def inner():
#         x = 1000
#         return x

#     return inner()

# print(outer(10))

# y=30
# print(globals())

# text = "I am global!"
# def foo():
#     text = "I am local!"
#     print(locals())
# foo()
# print(text)

# def foo():
#     x=1

# foo()
# print(x)

# def foo(x):
#     print(locals())

# foo(1)

# def foo(x, y=0):
#     return x-y

# print(foo(3, 1))
# print(foo(3))
# #print(foo())
# print(foo(y=1, x=3))

# def outer():
#     x = 1
#     def inner():
#         print(x)
#     inner()

# outer()

# print(issubclass(int, object))

# def foo():
#     pass
# print(foo.__class__)

# print(issubclass(foo.__class__, object))

# def add(x, y):
#     return x+y
# def sub(x, y):
#     return x-y
# def apply(func, x, y):
#     return func(x, y)

# print(apply(add, 2, 1))
# print(apply(sub, 2, 1))

# def outer():
#     def inner():
#         print("Inside inner")
#     return inner
# foo = outer()

# print(foo)
# foo()

# def outer(x):
#     def inner():
#         print(x)
#     return inner

# foo1 = outer(1)
# foo2 = outer(2)

# foo1()
# foo2()

# def outer(some_func):
#     def inner():
#         print("before some_func")
#         ret = some_func()
#         print(ret + 1)
#     return inner

# def foo():
#     return 1

# decorated = outer(foo)
# decorated()

# class Coordinate(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         return "Coord: " + str(self.__dict__)

# def wrapper(func):
#     def checker(a, b):
#         if a.x < 0 or a.y < 0:
#             a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
#         if b.x < 0 or b.y < 0:
#             b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
#         ret = func(a, b)
#         if ret.x < 0 or ret.y < 0:
#             ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
#         return ret
#     return checker

# @wrapper
# def add(a, b):
#     return Coordinate(a.x + b.x, a.y + b.y)
# @wrapper
# def sub(a, b):
#     return Coordinate(a.x - b.x, a.y - b.y)

# # add = wrapper(add)
# # sub = wrapper(sub)

# one = Coordinate(100, 200)
# two = Coordinate(300, 200)
# three = Coordinate(-100, -100)
# print(sub(one, two))
# print(add(one, three))


# def one(*args):
#     print(args)
# one()

# def two(x, y, *args):
#     print(x, y, args)
# two('a', 'b', 'c')

# def add(x, y):
#     return x + y
# lst = [1,2]
# print(add(lst[0], lst[1]))
# print(add(*lst))

# dct = {'x':1, 'y':2}
# def bar(x, y):
#     return x + y
# print(bar(**dct))

def logger(func):
    def inner(*args, **kwargs):
        print('Arguments were: %s, %s' % (args, kwargs))
        return func(*args, **kwargs)
    return inner

@logger
def foo1(x, y=1):
    return x*y

@logger
def foo2():
    return 2

print(foo1(5, 4))
print(foo1(1))
print(foo2())