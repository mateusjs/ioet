from enum import Enum


class TypeOfWeek(Enum):
    WEEK = "week"
    WEEKEND = "weekend"

LABORDAYS = ["MO", "TU", "WE", "TH", "FR"]
WEEKEND = ["SA", "SU"]

MAX_HOUR = 24

shifts = {
    "morning": {"week": 25, "weekend": 30},
    "evening": {"week": 15, "weekend": 20},
    "night": {"week": 20, "weekend": 25},
}
