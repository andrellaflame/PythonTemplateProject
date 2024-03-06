import unittest
import pandas as pd
from app.io.input import read_file_builtin, read_file_pandas


class TestInput(unittest.TestCase):
    def test_read_file_builtin(self):
        content = read_file_builtin('../data/input_files/input_file.txt')
        print(content)
        self.assertIsInstance(content, str)
        self.assertNotEqual(content, '')

        content = read_file_builtin('nonexistent_file.txt')
        self.assertIsNone(content)

    def test_read_file_pandas(self):
        data = read_file_pandas('../data/input_files/data.csv')
        self.assertIsInstance(data, pd.DataFrame)
        self.assertNotEqual(data.shape, (0, 0))

        data = read_file_pandas('nonexistent_data.csv')
        self.assertIsNone(data)


if __name__ == '__main__':
    unittest.main()
