import pytest
from decorators import log


@log("")
def example_function():
    raise Exception("Something went wrong!")


def test_exception_log():
    with pytest.raises(Exception, match="Something went wrong!"):
        example_function()
