import pandas as pd


def input_text():
    """
    Function to input text from the console.
    """
    text = input("Введіть текст: ")
    return text


def read_file_builtin(file_path):
    """
    Function to read text from a file using Python's built-in capabilities.

    Params:
    file_path (str): The path to the file to be read.

    Returns:
    str: Content read from the file.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print("Файл не знайдено")
        return None


def read_file_pandas(file_path):
    """
    Function to read data from a file using the pandas library.

    Params:
    file_path (str): The path to the file to be read.

    Returns:
    pandas.DataFrame: DataFrame containing the data read from the file.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("Файл не знайдено")
        return None
