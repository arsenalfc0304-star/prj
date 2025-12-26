import os
from time import time


def log(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time_1 = time()
            try:
                if not filename == "":
                    with open(filename, "r") as f:
                        with open(filename, "a") as file:
                            file.write(result + "\n")
                else:
                    print(result)
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                print(f"Retrying... ({e})")
            raise Exception(f"Something went wrong!")
            time_2 = time()

        return wrapper

    return decorator
