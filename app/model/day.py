from exceptions import HourShiftError, NoHoursFound
from model.hours_of_work import HoursOfWork
from model.helpers import WEEKEND, TypeOfWeek, shifts
from utils import get_the_shift


class Day:
    """
    Model that make easier to take control of a day
    
    """

    def __init__(self, day_initials: str):
        self.day_initials = day_initials
        self._type_of_week = self._get_week_type()

    def _get_week_type(self) -> str:
        if not self.day_initials:
            raise ValueError("day_initials cannot be None or empty")
        _type_of_week = TypeOfWeek.WEEK

        if self.day_initials in WEEKEND:
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
