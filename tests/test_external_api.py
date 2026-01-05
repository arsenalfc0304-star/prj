from unittest.mock import Mock, patch

from src.external_api import get_api_convertion_to_rub


def test_get_api_convertion_to_rub_success():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 999.9}

    with patch("requests.get", return_value=mock_response):
        result = get_api_convertion_to_rub(
            {
                "id": 560813069,
                "state": "CANCELED",
                "date": "2019-12-03T04:27:03.427014",
                "operationAmount": {"amount": "17628.50", "currency": {"name": "USD", "code": "USD"}},
            }
        )
        assert result == 999.9


def test_get_api_convertion_to_rub_fault():
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.json.return_value = {"result": 999.9}

    with patch("requests.get", return_value=mock_response):
        result = get_api_convertion_to_rub(
            {
                "id": 560813069,
                "state": "CANCELED",
                "date": "2019-12-03T04:27:03.427014",
                "operationAmount": {"amount": "17628.50", "currency": {"name": "USD", "code": "USD"}},
            }
        )
        assert result == 0
