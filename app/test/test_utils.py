import unittest
from unittest.mock import patch

from exceptions import FileWithBadFormation
from utils import (
    file_path_based_on_os,
    get_days_of_work,
    get_hours,
    get_name,
    get_the_shift
)


class TestUtils(unittest.TestCase):
    def test_should_get_name_with_success(self):
        name = get_name("MATEUS=12345")
        assert name == "MATEUS"

    def test_should_not_get_name_even_with_value_empty(self):
        name = get_name("")
        assert name == ""

    def test_should_get_days_of_work_with_success(self):
        days = get_days_of_work("ANTONIO=MO7:00-11:00,TU14:00-16:00")
        assert days == "MO7:00-11:00,TU14:00-16:00"

    def test_should_get_days_of_work_with_file_bad_formation_error(self):
        with self.assertRaises(FileWithBadFormation) as context:
            get_days_of_work("ANTONIO")
        self.assertTrue(
            "File has bad formation, validate your file data" in str(
                context.exception)
        )

    def test_should_get_hours_with_success(self):
        start, end = get_hours("10:00-12:00")
        assert start == 10
        assert end == 12

    def test_should_get_hours_with_value_error(self):
        with self.assertRaises(ValueError) as context:
            get_hours("")
        self.assertTrue(
            "invalid literal for int() with base 10: ''" in str(
                context.exception
            )
        )

    def test_should_get_hours_with_attribute_error(self):
        with self.assertRaises(AttributeError) as context:
            get_hours(None)
        self.assertTrue(
            "'NoneType' object has no attribute 'split'" in str(
                context.exception)
        )

    def test_should_get_the_shift_with_success(self):
        for i in range(1, 9):
            shift = get_the_shift(i)
            assert shift == "morning"
        for i in range(10, 18):
            shift = get_the_shift(i)
            assert shift == "day"
        for i in range(19, 25):
            if i == 24:
                shift = get_the_shift(0)
            shift = get_the_shift(i)
            assert shift == "night"

    @patch('utils.os.name', "java")
    def test_should_return_path_for_not_windows_with_success(self):
        expected_path = 'data/test.txt'
        file_path = file_path_based_on_os('test.txt')
        assert expected_path in file_path

    @patch('utils.os.name', "nt")
    def test_should_return_path_based_for_windows_with_success(self):
        expected_path = 'data\\test.txt'
        file_path = file_path_based_on_os('test.txt')
        assert expected_path in file_path
