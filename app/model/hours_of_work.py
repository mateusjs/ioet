from exceptions import HourShiftError
from model.helpers import MAX_HOUR
from utils import get_hours


class HoursOfWork:
    """
    Hours of work from an employee
    """

    def __init__(self, hours: str):
        self.start_time, self.end_time = get_hours(hours)
        self.set_start_and_end_times()

    def set_start_and_end_times(self):
        if self.start_time > MAX_HOUR or self.end_time > MAX_HOUR:
            raise HourShiftError(self.start_time, self.end_time)

        if self.start_time == 0:
            raise HourShiftError(self.start_time, self.end_time)

        if self.end_time == 0:
            self.end_time = 24

        if self.start_time > self.end_time:
            raise HourShiftError(self.start_time, self.end_time)