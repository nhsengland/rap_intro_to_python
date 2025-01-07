import pandas as pd
from my_new_function import multiply_numbers # If you edit the filename above, or change the function names remember to change your improt statement

def test_calculate_multiplication():
    """
    Test the calculate multiplication function for expected behavior.
    """
    # Arrange
    data = {"num1": [2], "num2": [3]}
    input_df = pd.DataFrame(data)

    expected = 6

    # Act
    actual = multiply_numbers(input_df, input_df["num1"][0], input_df["num2"][0])

    # Assert
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_calculate_multiplication_string():
    """
    Test the calculate multiplication function for strings
    """
    # Arrange
    data = {"num1": [2], "num2": ["three"]}
    input_df = pd.DataFrame(data)

    expected = None

    # Act
    actual = multiply_numbers(input_df, input_df["num1"][0], input_df["num2"][0])

    # Assert
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_calculate_multiplication_large():
    """
    Test the calculate multiplication function for large numbers
    """
    # Arrange
    data = {"num1": [2000000], "num2": [3000000]}
    input_df = pd.DataFrame(data)

    expected = 6000000000000

    # Act
    actual = multiply_numbers(input_df, input_df["num1"][0], input_df["num2"][0])

    # Assert
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_calculate_multiplication_small():
    """
    Test the calculate multiplication function for small numbers
    """
    # Arrange
    data = {"num1": [0.0000002], "num2": [0.0000003]}
    input_df = pd.DataFrame(data)

    expected = 0.00000000000006

    # Act
    actual = multiply_numbers(input_df, input_df["num1"][0], input_df["num2"][0])

    # Assert
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_calculate_multiplication_negative():
    """
    Test the calculate multiplication function for negative numbers
    """
    # Arrange
    data = {"num1": [-2], "num2": [3]}
    input_df = pd.DataFrame(data)

    expected = -6

    # Act
    actual = multiply_numbers(input_df, input_df["num1"][0], input_df["num2"][0])

    # Assert
    assert actual == expected, f"Expected {expected} but got {actual}"

