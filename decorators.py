import os


def log(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if os.path.exists(filename):
                with open(filename, "r") as f:
                    with open(f"{filename}.txt", "a") as file:
                        file.write(result + "\n")
            else:
                print(result)

        return wrapper

    return decorator
