import os
from time import time


def log(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time_1 = time()
            result = func(*args, **kwargs)
            time_2 = time()
            if not filename == "":
                with open(filename, "r") as f:
                    with open(filename, "a") as file:
                        file.write(result + "\n")
            else:
                print(result)

        return wrapper

    return decorator
