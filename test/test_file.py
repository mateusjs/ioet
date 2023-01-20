import unittest
from unittest.mock import patch
from exceptions import FileNotFound
import os

from file import get_file, read_file

correct_file = [
    "RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00",
    "ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00",
]

empty = []


class TestFiles(unittest.TestCase):
    @patch("file.read_file")
    def test_get_file_should_find_file_and_call_read_file(self, mock_read_file):
        mock_read_file.return_value = correct_file
        file = get_file()
        assert file == correct_file
        mock_read_file.assert_called_once()

    @patch('os.path.join')
    def test_get_file_with_error(self, mock_os):
        mock_os.return_value = ''
        with self.assertRaises(FileNotFoundError) as context:
            get_file()
        self.assertTrue(
            'No such file or directory' in str(context.exception)
        )
    
    def test_read_file(self):
        file_dir = os.path.join(os.getcwd(), 'data\\file.txt')
        file_lines = read_file(file_dir)
        assert file_lines

    def test_read_file_with_error(self):
         with self.assertRaises(FileNotFoundError) as context:
            read_file("")
         self.assertTrue(
            'No such file or directory' in str(context.exception)
        )