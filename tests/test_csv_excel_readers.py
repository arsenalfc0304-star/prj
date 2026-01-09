from unittest.mock import Mock, patch
import pytest

import pandas as pd

from src.csv_excel_readers import read_data_from_csv, read_data_from_excel


@pytest.fixture
def sample_df():
    sample_dict = {
        "id": [560813069, 560813069],
        "state": ["CANCELED", "CANCELED"],
        "date": ["2019-12-03T04:27:03.427014", "2019-12-03T04:27:03.427014"]
    }
    return pd.DataFrame(sample_dict)


def test_read_data_from_csv():
    mock_path = Mock()
    mock_path.return_value = sample_df
    with patch('path'):
    assert read_data_from_csv(mock_path) == (
        {
            "id": 560813069,
            "state": "CANCELED",
            "date": "2019-12-03T04:27:03.427014"

        },
        {
            "id": 560813069,
            "state": "CANCELED",
            "date": "2019-12-03T04:27:03.427014"
        }
    )