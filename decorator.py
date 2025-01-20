
# Decorator
# function that takes another function as its argument and gives it more functionality.


# import time


# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} ")
#         print("Runnning...")
#         return func(*args, **kwargs)
#     return wrapper


def another_decorator(func):
    def wrapper():
        print(f"Calling.... {func.__name__}")
        return func()
    return wrapper


@another_decorator
def say_hello():
    print("Hello everyone")


say_hello()


# @my_decorator
# def multiply(a, b):
#     time.sleep(1.5)
#     print("Result :", a * b)


# multiply(5, 4)
