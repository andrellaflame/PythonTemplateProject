import pandas as pd


def input_text():
    text = input("Введіть текст: ")
    return text


def read_file_builtin(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print("Файл не знайдено")
        return None


def read_file_pandas(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("Файл не знайдено")
        return None
