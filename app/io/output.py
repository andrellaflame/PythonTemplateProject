import os


def output_text(text):
    """
    Function to output text to the console.

    Params:
    text (str): The text to be output.
    """
    print("Текст:", text)


def write_file_builtin(filename, content):
    """
    Function to write content to a file using Python's built-in capabilities.

    Params:
    file_path (str): The path to the file to be written.
    content (str): The content to be written to the file.
    """
    data_folder = 'data'
    file_path = os.path.join(data_folder, filename)

    with open(file_path, 'w') as file:
        file.write(content)
