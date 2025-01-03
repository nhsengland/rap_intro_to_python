
def multiply_numbers(input_1, input_2):
    if isinstance(input_1, str):
        print(f"Error: {input_1} is a string")
        return None
    if isinstance(input_2, str):
        print(f"Error: {input_2} is a string")
        return None
    output_val = input_1 * input_2
    return output_val
