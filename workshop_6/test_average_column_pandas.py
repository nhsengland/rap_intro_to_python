#^Very import to start your file and functions with "test" - this is how pytest finds them!
import pandas as pd
from average_column_function_pandas import calculate_average # You will need to import your function to test it!


def test_calculate_average():
    """
    Test the calculate average function for expected behavior.
    """
    # Arrange
    data = {"value": ["100", "200", "300"]}
    input_df = pd.DataFrame(data)

    expected = 200.0

    # Act
    actual = calculate_average(input_df, "value")

    # Assert
    assert actual == expected, f"Expected {expected} but got {actual}"


def test_calculate_average_empty_df():
    """
    Test the calculate average function for an empty DataFrame.
    """
    # Arrange
    data = {}  # Empty dictionary
    input_df = pd.DataFrame(data)

    expected = None

    # Act
    actual = calculate_average(input_df, "value")

    # Assert
    assert actual == expected, f"Expected {expected} but got {actual}"


def test_calculate_average_no_column():
    """
    Test the calculate average function for a column that doesn't exist.
    """
    # Arrange
    data = {"value": ["100", "200", "300"]}
    input_df = pd.DataFrame(data)

    expected = None

    # Act
    actual = calculate_average(input_df, "age")

    # Assert
    assert actual == expected, f"Expected {expected} but got {actual}"


def test_calculate_average_currency_inputs():
    """
    Test the calculate average function for a column containing currency values.
    """
    # Arrange
    data = {"value": ["£100", "£200", "£300"]}
    input_df = pd.DataFrame(data)

    expected = 200.0

    # Act
    actual = calculate_average(input_df, "value")

    # Assert
    assert actual == expected, f"Expected {expected} but got {actual}"
