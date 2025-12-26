import os
from time import time


def log():
    def decorator(func):
        def wrapper(*args, **kwargs):
           # time_1 = time()
            try:
                result = func(*args, **kwargs)
                # if not filename == "":
                #     with open(filename, "r") as f:
                #         with open(filename, "a") as file:
                #             file.write(result + "\n")
                # else:
            except Exception as e:
                raise Exception(f"Max retries exceeded")
           # time_2 = time()
            return result
            print(time_1)
            print(time_2)

        return wrapper

    return decorator
#
# @log()
# def example_func(a, b):
#     return a / b
#
# example_func(5, 2)