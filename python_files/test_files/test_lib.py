"""
Testing the library file functions

"""

import io
import sys

sys.path.append("python_files")

from python_files.lib import (
    load_dataset,
    full_describe,
    build_bar_chart,
)

# Shortened mock CSV data as a string (only "year" and "fatal" columns)
mock_csv_data = """
,less_than_hs,high_school,some_college,bachelors_degree,advanced_degree
12.00,16.00,20.00,24.00,40.00
14.00,18.00,22.00,28.00,45.00
16.00,20.00,24.00,30.00,50.00
18.00,22.00,26.00,35.00,55.00
20.00,24.00,28.00,40.00,60.00
"""
test_path = io.StringIO(mock_csv_data)


def test_load_dataset():
    """test that loading the CSV will work"""
    result = load_dataset(test_path)
    assert result is not None
    assert result.shape == (5, 4)


def test_full_describe():
    test_path = io.StringIO(mock_csv_data)
    test_df = load_dataset(test_path)

    result = full_describe(test_df)
    assert result is not None


def test_build_bar_chart():
    test_path = io.StringIO(mock_csv_data)
    test_df = load_dataset(test_path)

    result = build_bar_chart(test_df, False)
    assert result is None


if __name__ == "__main__":
    test_load_dataset()
    test_full_describe()
    test_build_bar_chart()
