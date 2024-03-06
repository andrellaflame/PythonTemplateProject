from app.io.input import input_text, read_file_builtin, read_file_pandas
from app.io.output import output_text, write_file_builtin


def main():
    text_input = input_text()

    file_content_builtin = read_file_builtin('data/input_files/input_file.txt')
    file_data_pandas = read_file_pandas('data/input_files/data.csv')

    output_text(text_input)
    output_text(file_content_builtin)
    output_text(file_data_pandas)

    if file_content_builtin is not None:
        write_file_builtin('output_file_builtin.txt', file_content_builtin)
    else:
        print("Cannot write to file. File content is None.")

    write_file_builtin('output_file.txt', text_input)


if __name__ == '__main__':
    main()
