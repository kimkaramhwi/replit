# lambda : 인라인 함수를 정의할 때 사용하며 익명 함수 또는 람다 표현식이라고 부른다.

# f = lambda x,y,z : x+y+z

# print(f)
# print(f(1,2,3))

# Lambdas = [
#     lambda x : x ** 2,
#     lambda x : x ** 3,
#     lambda x : x ** 4
# ]
# for lambda_func in Lambdas:
#     print(lambda_func(2))

# import types
# f = lambda x,y,z : x+y+z

# print(f)
# print(type(f))
# print(type(f) == types.LambdaType)


lambdas = [
    lambda password : "SHORT_PASSWORD" if len(password) < 8 else None,
    lambda password : "NO_CAPITAL_LETTER_PASSWORD" if not any(c.isupper() for c in password) else None
]

def check_password_using_lambda(password):
    for f in lambdas:
        if f(password) is not None:
            return f(password)
    return True

print(check_password_using_lambda('123'))
print(check_password_using_lambda('12356789f'))
print(check_password_using_lambda('123456789F'))