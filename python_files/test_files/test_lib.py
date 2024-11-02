"""
Testing the library file functions

"""

import io
import sys

sys.path.append("python_files")

from python_files.lib import (
    load_dataset,
    full_describe,
    mens_bar_chart,
    womens_bar_chart,
)

# Shortened mock CSV data as a string (only "year" and "fatal" columns)
mock_csv_data = """year,less_than_hs,high_school,some_college,bachelors_degree,advanced_degree
2010,12.50,15.00,17.50,22.50,30.00
2011,2.75,15.25,17.75,22.75,30.50
2012,13.00,15.50,18.00,23.00,31.00
2013,13.25,15.75,18.25,23.25,31.50
2014,13.50,16.00,18.50,23.50,32.00"""

mock_mens_data = """year,men_less_than_hs,men_high_school,men_some_college,men_bachelors_degree,men_advanced_degree
2000,13.00,16.00,18.50,24.00,32.00
2001,13.25,16.25,18.75,24.25,32.50
2002,13.50,16.50,19.00,24.50,33.00
2003,13.75,16.75,19.25,24.75,33.50
2004,14.00,17.00,19.50,25.00,34.00
"""

mock_womens_data = """year,women_less_than_hs,women_high_school,women_some_college,women_bachelors_degree,women_advanced_degree
2000,12.50,15.50,18.00,23.50,31.50
2001,12.75,15.75,18.25,23.75,31.75
2002,13.00,16.00,18.50,24.00,32.00
2003,13.25,16.25,18.75,24.25,32.25
2004,13.50,16.50,19.00,24.50,32.50
"""

full_test_path = io.StringIO(mock_csv_data)
mens_test_path = io.StringIO(mock_mens_data)
womens_test_path = io.StringIO(mock_womens_data)


def test_load_dataset():
    """test that loading the CSV will work"""
    result = load_dataset(full_test_path)
    assert result is not None
    assert result.shape == (5, 6)


def test_full_describe():
    test_path = io.StringIO(mock_csv_data)
    test_df = load_dataset(test_path)
    result = full_describe(test_df)
    assert result is not None


def test_mens_bar_chart():
    test_path = io.StringIO(mock_mens_data)
    test_df = load_dataset(test_path)
    result = mens_bar_chart(test_df, False)
    assert result is None


def test_womens_bar_chart():
    test_path = io.StringIO(mock_womens_data)
    test_df = load_dataset(test_path)
    result = womens_bar_chart(test_df, False)
    assert result is None


if __name__ == "__main__":
    test_load_dataset()
    test_full_describe()
    test_mens_bar_chart()
    test_womens_bar_chart()
