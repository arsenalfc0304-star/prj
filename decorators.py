def log(filename=""):
    """
    автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки,
    принимает необязательный аргумент filename, который определяет, куда будут записываться логи (в файл или в консоль)
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename == "":
                    print(f"{func.__name__} ok")
                else:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok\n")
                return result
            except Exception as e:
                if filename == "":
                    print(f"{func.__name__} error: {e}. Inputs: ({args}, {kwargs})")
                else:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: ({args}, {kwargs})\n")

        return wrapper

    return decorator
