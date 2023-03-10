import unittest

from exceptions import NoHoursFound
from model.day import Day
from model.enums import TypeOfWeek
from model.helpers import LABORDAYS, WEEKEND


class TestDay(unittest.TestCase):
    def test_day_class_instance(self):
        day_of_work = "TH12:00-14:00"
        day_initials = day_of_work[:2]
        day = Day(day_initials)
        assert isinstance(day, Day)
        assert hasattr(day, "day_initials")
        assert hasattr(day, "_type_of_week")
        assert day._type_of_week == TypeOfWeek.WEEK

    def test_get_week_type_with_labor_days_success(self):
        for abbreviation in LABORDAYS:
            day = Day(abbreviation)
            assert day._type_of_week == TypeOfWeek.WEEK

    def test_get_week_type_with_weekend_days_success(self):
        for abbreviation in WEEKEND:
            day = Day(abbreviation)
            assert day._type_of_week == TypeOfWeek.WEEKEND

    def test_get_week_type_with_value_error_day_none(self):
        with self.assertRaises(ValueError) as context:
            Day(None)
        self.assertTrue(
            "day_initials cannot be None or empty" in str(context.exception)
        )

    def test_get_week_type_with_value_error_day_empty(self):
        with self.assertRaises(ValueError) as context:
            Day("")
        self.assertTrue(
            "day_initials cannot be None or empty" in str(context.exception)
        )

    def test_calculate_day_cost_with_success(self):
        day_of_work = "TH12:00-14:00"
        day_times = day_of_work[2:]
        day_initials = day_of_work[:2]
        day = Day(day_initials)
        cost = day.calculate_day_cost(day_times)
        assert cost == 30

    def test_calculate_day_cost_with_error(self):
        day_of_work = "TH14:"
        day_initials = day_of_work[:2]
        day = Day(day_initials)
        with self.assertRaises(NoHoursFound) as context:
            day.calculate_day_cost("")
        self.assertTrue(
            "The actual day has no hours" in str(context.exception)
        )
