import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("string, expected_result", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Сет 35383033474447895560", "Номер введен некорректно"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("5999414228426353", "Номер введен некорректно"),
    ("", "Номер введен некорректно")
])
def test_mask_account_card(string: str, expected_result: str) -> str:
    assert mask_account_card(string) == expected_result


@pytest.mark.parametrize("string, expected_result", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2024-13-11T02:26:18.671407", "Дата введена некорректно"),
    ("20240311", "Дата введена некорректно"),
    ("a024-03-11", "Дата введена некорректно"),
    ("", "Дата введена некорректно")
])
def test_get_date(string: str, expected_result: str) -> str:
    assert get_date(string) == expected_result
