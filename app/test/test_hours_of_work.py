import unittest
from exceptions import HourShiftError
from model.hours_of_work import HoursOfWork


class TestHoursOfWork(unittest.TestCase):
    def test_hours_of_work_creation_with_success(self):
        hours = "10:00-19:00"
        hours_of_work = HoursOfWork(hours)
        assert isinstance(hours_of_work, HoursOfWork)
        assert hasattr(hours_of_work, "start_time")
        assert hasattr(hours_of_work, "end_time")

    def test_hours_of_work_creation_with_success_and_midnight_as_00(self):
        hours = "10:00-00:00"
        hours_of_work = HoursOfWork(hours)
        assert hours_of_work.start_time == 10
        assert hours_of_work.end_time == 24

    def test_hours_of_work_creation_hour_shift_error_with_start_time_greater_than_end_time(
        self,
    ):
        hours = "22:00-19:00"
        with self.assertRaises(HourShiftError) as context:
            HoursOfWork(hours)
        self.assertTrue("(22, 19)" in str(context.exception))

    def test_hours_of_work_creation_hour_shift_error_with_start_time_greater_than_max_time(
        self,
    ):
        hours = "25:00-19:00"
        with self.assertRaises(HourShiftError) as context:
            HoursOfWork(hours)
        self.assertTrue("(25, 19)" in str(context.exception))

    def test_hours_of_work_creation_hour_shift_error_with_end_time_greater_than_max_time(
        self,
    ):
        hours = "12:00-25:00"
        with self.assertRaises(HourShiftError) as context:
            HoursOfWork(hours)
        self.assertTrue("(12, 25)" in str(context.exception))

    def test_hours_of_work_creation_hour_shift_error_with_start_time_equals_to_zero(
        self,
    ):
        hours = "00:00-12:00"
        with self.assertRaises(HourShiftError) as context:
            HoursOfWork(hours)
        self.assertTrue("(0, 12)" in str(context.exception))
