a = 1
b = a
c = 1
d = 2

if a == b: # True
    print('True')
else:
    print('False')

if a == d: # False
    print('True')
else:
    print('False')

if a is b: # True
    print('True')
else:
    print('False')

if a is c: # True
    print(hex(id(a)))
    print(hex(id(c)))
    print('True')
else:
    print('False')

if a is d: # False
    print('True')
else:
    print(hex(id(a)))
    print(hex(id(d)))
    print('False')

if a: # True
    print('True')
else:
    print('False')
