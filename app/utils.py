from exceptions import FileWithBadFormation


def get_name(text_line: str) -> str:
    return text_line.split("=")[0]


def get_days_of_work(text_line: str) -> str:
    try:
        return text_line.split("=")[1].replace('\n', '')
    except:
        raise FileWithBadFormation("File has bad formation, validate your data")


def get_hours(hours: str):
    try:
        return int(hours.split("-")[0].split(":")[0]), int(
            hours.split("-")[1].split(":")[0]
        )
    except ValueError:
        raise

def get_the_shift(hour):
    if hour > 0 and hour <= 9:
        return "morning"
    if hour > 9 and hour <= 18:
        return "evening"
    return "night"