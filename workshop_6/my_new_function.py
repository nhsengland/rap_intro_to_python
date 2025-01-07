
def multiply_numbers(df, num1, num2):
    """
    Multiply 2 numbers together

    :param df: Input DataFrame
    :param num1: The first number to be multiplied
    :param num2: The second number to be multiplied
    :return: The multiplication sum of the 2 numbers
    """
    print("hello1")
    # Check if the DataFrame is empty
    if df.empty:
        print("Error: The DataFrame is empty.")
        return None
    
    # Check if values entered are numeric
    print("hello")
    
    try:
        num1=float(num1)
        num2=float(num2)
    except ValueError:
        print(f"Error: non-numeric value entered")
        return None

   
    # Calculate the multiplication sum
    result = num1 * num2
    
    return result
