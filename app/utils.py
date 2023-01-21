from typing import Tuple
from exceptions import FileWithBadFormation
import os


def file_path_based_on_os(file_name: str) -> str:
    if os.name == 'nt':
        return f'data\\{file_name}'
    return f'data/{file_name}'


def get_name(text_line: str) -> str:
    return text_line.split("=")[0]


def get_days_of_work(text_line: str) -> str:
    try:
        return text_line.split("=")[1].replace('\n', '')
    except:
        raise FileWithBadFormation(
            "File has bad formation, validate your file data")


def get_hours(hours: str) -> Tuple[int, int]:
    try:
        return int(hours.split("-")[0].split(":")[0]), int(
            hours.split("-")[1].split(":")[0]
        )
    except ValueError:
        raise


def get_the_shift(hour) -> str:
    if hour > 0 and hour <= 9:
        return "morning"
    if hour > 9 and hour <= 18:
        return "evening"
    return "night"
