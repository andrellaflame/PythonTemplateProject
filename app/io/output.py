def output_text(text):
    print("Текст:", text)


def write_file_builtin(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
