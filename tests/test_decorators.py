import pytest


def test_log(capsys):
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"


@retry_decorator(max_retries=3)
def example_function():
    # some potentially failing operation
    raise ValueError("Something went wrong!")


def test_retry_decorator():
    with pytest.raises(Exception, match="Max retries exceeded"):
        example_function()
