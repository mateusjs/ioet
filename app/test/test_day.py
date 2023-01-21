import unittest
from unittest.mock import patch
from exceptions import NoHoursFound
from model.day import Day
from helpers import TypeOfWeek, LABORDAYS, WEEKEND


class TestDay(unittest.TestCase):
    def test_day_class_instance(self):
        day_of_work = "TH12:00-14:00"
        day_abbreviation = day_of_work[:2]
        day = Day(day_abbreviation)
        assert isinstance(day, Day)
        assert hasattr(day, "day_abbreviation")
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
            "day_abbreviation cannot be None or empty" in str(context.exception)
        )

    def test_get_week_type_with_value_error_day_empty(self):
        with self.assertRaises(ValueError) as context:
            Day("")
        self.assertTrue(
            "day_abbreviation cannot be None or empty" in str(context.exception)
        )

    def test_calculate_day_cost_with_success(self):
        day_of_work = "TH12:00-14:00"
        day_times = day_of_work[2:]
        day_abbreviation = day_of_work[:2]
        day = Day(day_abbreviation)
        cost = day.calculate_day_cost(day_times)
        assert cost == 30

    def test_calculate_day_cost_with_error(self):
        day_of_work = "TH14:"
        day_abbreviation = day_of_work[:2]
        day = Day(day_abbreviation)
        with self.assertRaises(NoHoursFound) as context:
            day.calculate_day_cost("")
        self.assertTrue("The actual day has no hours" in str(context.exception))
