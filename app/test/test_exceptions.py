import unittest

from exceptions import (
    BlankFile,
    FileNotFound,
    FileWithBadFormation,
    HoursShiftError,
    NoHoursFound
)


class TestExceptions(unittest.TestCase):
    def test_blank_file(self):
        with self.assertRaises(Exception) as context:
            raise BlankFile("File has no content")
        self.assertTrue("File has no content" in str(context.exception))

    def test_file_not_found(self):
        with self.assertRaises(Exception) as context:
            raise FileNotFound("File not found")
        self.assertTrue("File not found" in str(context.exception))

    def test_file_with_bad_formation(self):
        with self.assertRaises(Exception) as context:
            raise FileWithBadFormation("File with bad formation")
        self.assertTrue("File with bad formation" in str(context.exception))

    def test_hour_shift_error(self):
        with self.assertRaises(Exception) as context:
            raise HoursShiftError("Hour shift error")
        self.assertTrue("Hour shift error" in str(context.exception))

    def test_no_hours_found(self):
        with self.assertRaises(Exception) as context:
            raise NoHoursFound("No hours found")
        self.assertTrue("No hours found" in str(context.exception))
