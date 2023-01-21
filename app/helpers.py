from enum import Enum


class TypeOfWeek(Enum):
    WEEK = "week"
    WEEKEND = "weekend"


ONE_MINUTE = 1 / 60

SUCCESS = 1
FAIL = 0

FILE_NOT_FOUND = "File not found.\nBe sure the file exists."
MALFORMED_FILE = "File is malformed, please check the file"
WRONG_TIME_RANGE = "Invalid range of hours"
EMPTY_FILE = "File is empty"

LABORDAYS = ["MO", "TU", "WE", "TH", "FR"]
WEEKEND = ["SA", "SU"]

MIN_HOUR = 0
MAX_HOUR = 24


shifts = {
    "morning": {"week": 25, "weekend": 30},
    "evening": {"week": 15, "weekend": 20},
    "night": {"week": 20, "weekend": 25},
}
