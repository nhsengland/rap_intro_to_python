
from suppress2.py import suppress2

def test_suppress2_int():
    #Testing for expected behaviour with integer
    #Arrange
    vals = 4

    expected = None

    #Act
    actual = suppress2(4)

    #Assert
    assert actual == expected, f"Expected {expected} but got {actual}"
    
def test_suppress2_float():
    #Testing for expected behaviour with float
    #Arrange
    vals = 4.5

    expected = None

    #Act
    actual = suppress2(4.5)

    #Assert
    assert actual == expected, f"Expected {expected} but got {actual}"
    
def test_suppress2_str():
    #Testing for expected behaviour with string
    #Arrange
    vals = "Hello"

    expected = None

    #Act
    actual = suppress2("Hello")

    #Assert
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_suppress2_list_str():
    #Testing for expected behaviour with string value inside list
    #Arrange
    vals = [7, 0, -1.5, "Hello"]

    expected = [5, 0, 0, "Not a number"]

    #Act
    actual = suppress2([7, 0, -1.5, "Hello"])

    #Assert
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_suppress2_list_nums():
    #Testing for expected behaviour with list of numbers
    #Arrange
    vals = [-3, -0.5, 2, 8.4]

    expected = [0, 0, 0, 10]

    #Act
    actual = suppress2([-3, -0.5, 2, 8.4])

    #Assert
    assert actual == expected, f"Expected {expected} but got {actual}"
