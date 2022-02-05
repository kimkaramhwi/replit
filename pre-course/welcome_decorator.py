# 예를 들어, 다음 처럼 정의 하여 welcome_decorator decorator를 적용하여 greeting을 호출하면
# "Hello, welcome to WECODE!"

def welcome_decorator(func):
    def wrapper():
        return func() + "welcome to WECODE!"
    return wrapper

@welcome_decorator
def greeting():
    return "Hello, "

print(greeting())