from exceptions import NoHoursFound
from model.enums import TypeOfWeek
from model.helpers import WEEKEND, shifts
from model.hours import Hours
from utils import get_the_shift


class Day:
    """Class tha represent a day with 24 hours
    Args:
        day_initials (str): initials of a day
    Returns:
        TypeOfWeek: Return if the current day a
        week or weekend day

        Float: Return the total cost of the day
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

        work = Hours(hours)

        total = 0
        start = work.start_time + 1
        while start <= work.end_time:
            shift = get_the_shift(start)
            multiplier = shifts[shift][self._type_of_week.value]
            total += 1 * multiplier
            start += 1
        return total
