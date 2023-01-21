from exceptions import HourShiftError, NoHoursFound
from model.hours_of_work import HoursOfWork
from helpers import WEEKEND, TypeOfWeek, shifts
from utils import get_the_shift


class Day:
    """
    A period of 24 hours beginning at midnight,
    one of the seven time periods that make up a week.
    """

    def __init__(self, day_abbreviation: str):
        self.day_abbreviation = day_abbreviation
        self._type_of_week = self._get_week_type()

    def _get_week_type(self) -> str:
        if not self.day_abbreviation:
            raise ValueError("day_abbreviation cannot be None or empty")
        _type_of_week = TypeOfWeek.WEEK

        if self.day_abbreviation in WEEKEND:
            _type_of_week = TypeOfWeek.WEEKEND

        return _type_of_week

    def calculate_day_cost(self, hours: str) -> float:
        if not hours:
            raise NoHoursFound("The actual day has no hours")

        work = HoursOfWork(hours)

        total = 0
        start = work.start_time + 1
        while start <= work.end_time:
            shift = get_the_shift(start)
            multiplier = shifts[shift][self._type_of_week.value]
            total += 1 * multiplier
            start += 1
        return total
