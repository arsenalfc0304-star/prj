import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("string, expected_result", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("MasterCard 7158300734726758", "Номер введен некорректно"),
    ("Сет 35383033474447895560", "Номер введен некорректно"),
    ("Visa Classic 6831982476737658", "Номер введен некорректно"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("5999414228426353", "Номер введен некорректно")
])
def test_mask_account_card(string: str, expected_result: str) -> str:
    assert mask_account_card(string) == expected_result
