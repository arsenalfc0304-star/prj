from src.masks import get_mask_card_number, get_mask_account

import pytest

@pytest.mark.parametrize("string, expected_result", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("70007922896063611", "Номер карты введен некорректно"),
    ("700079228960636A", "Номер карты введен некорректно"),
    ("", "Номер карты введен некорректно"),
])
def test_get_mask_card_number(string, expected_result):
    assert get_mask_card_number(string) == expected_result


@pytest.mark.parametrize("string, expected_result", [
    ("7000792289606361", "**6361"),
    ("700079228960636A", "Номер счета введен некорректно"),
    ("", "Номер счета введен некорректно"),
])
def test_get_mask_account(string, expected_result):
    assert get_mask_account(string) == expected_result