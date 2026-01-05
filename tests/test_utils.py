from unittest.mock import Mock, patch

import pytest

from src.utils import load_json, transaction_rub
from src.external_api import get_api_convertion_to_rub


def test_load_json():
    assert load_json("data/operations1.json") == []
    assert (load_json("data/operations.json")[0]) == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def test_transaction_1() -> dict:
    return {
        "id": 560813069,
        "state": "CANCELED",
        "date": "2019-12-03T04:27:03.427014",
        "operationAmount": {"amount": "17628.50", "currency": {"name": "RUB", "code": "RUB"}},
    }


def test_transaction_rub_local(test_transaction_1) -> float:
    assert transaction_rub(test_transaction_1) == 17628.50


@pytest.fixture
def test_transaction_2() -> dict:
    return {
        "id": 560813069,
        "state": "CANCELED",
        "date": "2019-12-03T04:27:03.427014",
        "operationAmount": {"amount": "17628.50", "currency": {"name": "USD", "code": "USD"}},
    }


def test_transaction_rub_external(test_transaction_2) -> float:
    get_api_convertion_to_rub = Mock(return_value=5.55)

    assert transaction_rub(test_transaction_2) == 5.55
