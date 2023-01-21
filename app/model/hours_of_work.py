from exceptions import HourShiftError
from helpers import MAX_HOUR, MIN_HOUR
from utils import get_hours


class HoursOfWork:
    """
    Hours of work from an employee
    """

    def __init__(self, hours: str):
        self.start_time, self.end_time = get_hours(hours)
        self._check_hours()

    def _check_hours(self):
        if self.start_time == 0:
            raise HourShiftError(self.start_time, self.end_time)

        if self.end_time == 0:
            self.end_time = 24.0

        if self.start_time > MAX_HOUR or self.end_time > MAX_HOUR:
            raise HourShiftError(self.start_time, self.end_time)

        if self.start_time > self.end_time:
            raise HourShiftError(self.start_time, self.end_time)