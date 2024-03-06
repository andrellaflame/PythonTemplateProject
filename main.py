from app.io.input import input_text, read_file_builtin, read_file_pandas
from app.io.output import output_text, write_file_builtin


def main():
    text_input = input_text()

    file_content_builtin = read_file_builtin('data/input_file.txt')
    file_data_pandas = read_file_pandas('data/data.csv')

    output_text(text_input)
    output_text(file_content_builtin)
    output_text(file_data_pandas)

    write_file_builtin('data/output_file.txt', text_input)
    write_file_builtin('data/output_file_builtin.txt', file_content_builtin)

if __name__ == '__main__':
    main()
