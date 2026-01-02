from decorators import log


@log()
def example_func(a, b):
    return a / b


def test_log(capsys):
    example_func(4, 5)
    captured = capsys.readouterr()
    assert captured.out == "example_func ok\n"


def test_exception_log(capsys):
    example_func(4, 0)
    captured = capsys.readouterr()
    assert captured.out == "example_func error: division by zero. Inputs: ((4, 0), {})\n"
