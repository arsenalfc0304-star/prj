from unittest.mock import Mock, patch

from src.external_api import get_api_convertion_to_rub
from src.utils import load_json


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


def test_get_api_convertion_to_rub_success():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 999.9}

    with patch("requests.get", return_value=mock_response):
        result = get_api_convertion_to_rub(99.9, "USD")
        assert result == 999.9


def test_get_api_convertion_to_rub_fault():
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.json.return_value = {"result": 999.9}

    with patch("requests.get", return_value=mock_response):
        result = get_api_convertion_to_rub(99.9, "USD")
        assert result == 0
