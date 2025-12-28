def log(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename == "":
                    print(f"{func.__name__} ok")
                else:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok\n")
            except Exception as e:
                if filename == "":
                    print(f"{func.__name__} error: {e}. Inputs: ({args}, {kwargs})")
                else:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: ({args}, {kwargs})\n")

        return wrapper

    return decorator

@log("")
def example_func(a, b):
    return a / b

example_func(5, 0)