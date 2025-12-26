import pytest
from decorators import log


def test_log():
    @log
    def func(a, b):
        return a / b

    result = func(4, 2)
    assert result == 2.0
    # with pytest.raises(Exception, match="Something went wrong!"):
    #     example_function()

def test_exception_log():
    @log
    result = func(4, 0)
    with pytest.raises(Exception, match="Something went wrong!")
