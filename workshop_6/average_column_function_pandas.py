# This is writing this cell to a flat python file - this is the final function we are testing
import pandas as pd

def calculate_average(df, column_name):
    """
    Calculate the average of a specified column in a pandas DataFrame.

    :param df: Input DataFrame
    :param column_name: Name of the column to calculate the average for
    :return: The average value of the column
    """
    # Check if the DataFrame is empty
    if df.empty:
        print("Error: The DataFrame is empty.")
        return None
    
    # Check if column exists
    if column_name not in df.columns:
        print(f"Error: Column '{column_name}' not found in the DataFrame.")
        return None
    
    # Remove non-numeric characters (like currency symbols) and convert to float
    try:
        df[column_name] = df[column_name].replace(r"[^0-9.]", "", regex=True).astype(float)
    except ValueError:
        print(f"Error: Unable to convert values in column '{column_name}' to numeric.")
        return None
    
    # Calculate the average value
    avg_value = df[column_name].mean()
    
    return avg_value
