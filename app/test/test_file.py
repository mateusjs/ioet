import sys
import unittest
import os
import io
from unittest.mock import patch
from exceptions import BlankFile
from utils import file_path_based_on_os
from file_management import find_employee_on_file, get_file, read_file

correct_file = [
    "RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00",
    "ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00",
]


class TestFiles(unittest.TestCase):
    @patch("file_management.read_file")
    def test_get_file_should_find_file_and_call_read_file(self, mock_read_file):
        mock_read_file.return_value = correct_file
        file = get_file()
        assert file == correct_file
        mock_read_file.assert_called_once()

    @patch("os.path.join")
    def test_should_get_file_with_error(self, mock_os):
        mock_os.return_value = ""
        with self.assertRaises(FileNotFoundError) as context:
            get_file()
        self.assertTrue("No such file or directory" in str(context.exception))

    def test_shoudl_read_file_with_success(self):
        file_dir = os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)
            ),
            file_path_based_on_os('file.txt')
        )
        file_lines = read_file(file_dir)
        assert file_lines

    def test_shoudl_read_file_with_blank_file_error(self):
        file_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            file_path_based_on_os(
                'empty_file_test.txt'
            )
        )
        with self.assertRaises(BlankFile) as context:
            read_file(file_dir)
        self.assertTrue("File has no content" in str(context.exception))

    def test_should_read_file_with_error(self):
        with self.assertRaises(FileNotFoundError) as context:
            read_file("")
        self.assertTrue("No such file or directory" in str(context.exception))

    @patch("file_management.get_file")
    def test_should_find_employee_on_file_with_success(self, mock_get_file):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        mock_get_file.return_value = correct_file
        find_employee_on_file()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().split("\n")
        assert output[0] == "The amount to pay RENE is: 215.0 USD"
        assert output[1] == "The amount to pay ASTRID is: 85.0 USD"
