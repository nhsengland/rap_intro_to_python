
from my_new_function import multiply_numbers

def test_multiply_numbers():
    #testing for expected behaviour with positive integers
    # Arrange
    input_1 = 2
    input_2 = 5

    expected = 10
    
    # Act
    actual = multiply_numbers(2, 5)

    #Assert
    assert actual == expected, f"Expected {expected} but got {actual}"


def test_multiply_numbers_small():
    #testing for expected behaviour with decimal values below 1
    # Arrange
    input_1 = 0.1
    input_2 = .5

    expected = 0.05
    
    # Act
    actual = multiply_numbers(0.1, .5)

    #Assert
    assert actual == expected, f"Expected {expected} but got {actual}"


def test_multiply_numbers_negative():
    #testing for expected behaviour with a negative integer
    # Arrange
    input_1 = -2
    input_2 = 5

    expected = -10
    
    # Act
    actual = multiply_numbers(-2, 5)

    #Assert
    assert actual == expected, f"Expected {expected} but got {actual}"


def test_multiply_numbers_string():
    #testing for expected behaviour where one value is a string
    # Arrange
    input_1 = 2
    input_2 = "hello"

    expected = None
    
    # Act
    actual = multiply_numbers(2, "hello")

    #Assert
    assert actual == expected, f"Expected {expected} but got {actual}"

# If you edit the filename above, or change the function names remember to change your improt statement
