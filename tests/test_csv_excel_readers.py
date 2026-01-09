from unittest.mock import Mock, patch

import pandas as pd
import pytest

from src.csv_excel_readers import read_data_from_csv, read_data_from_excel


@pytest.fixture
def sample_df():
    sample_dict = {"id": [1, 2], "state": ["CANCELED", "CANCELED"]}
    return pd.DataFrame(sample_dict)


def test_read_data_from_csv_with_mock(sample_df):
    mock_read_csv = Mock(return_value=sample_df)
    pd.read_csv = mock_read_csv
    result = read_data_from_csv("data/transactions.csv")
    assert result == [{"id": 1, "state": "CANCELED"}, {"id": 2, "state": "CANCELED"}]


def test_read_data_from_csv_with_patch(sample_df):
    with patch("src.csv_excel_readers.pd.read_csv", return_value=sample_df):
        result = read_data_from_csv("data/transactions.csv")
        assert result == [{"id": 1, "state": "CANCELED"}, {"id": 2, "state": "CANCELED"}]


def test_read_data_from_excel_with_mock(sample_df):
    mock_read_excel = Mock(return_value=sample_df)
    pd.read_excel = mock_read_excel
    result = read_data_from_excel("data/transactions_excel.xlsx")
    assert result == [{"id": 1, "state": "CANCELED"}, {"id": 2, "state": "CANCELED"}]


def test_read_data_from_excel_with_patch(sample_df):
    with patch("src.csv_excel_readers.pd.read_excel", return_value=sample_df):
        result = read_data_from_excel("data/transactions_excel.xlsx")
        assert result == [{"id": 1, "state": "CANCELED"}, {"id": 2, "state": "CANCELED"}]
