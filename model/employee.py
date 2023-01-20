from exceptions import FileWithBadFormation
from model.day import Day


class Employee:
    salary = 0

    def __init__(self, name, days_worked):
        self.name = name
        self.days_worked = days_worked

    def __str__(self) -> str:
        pass

    def calculate_salary(self) -> float:
        salary: float = 0.0
        days_of_work = self.days_worked.split(",")
        if "" in days_of_work:
            raise FileWithBadFormation("Error obtaining datetimes")
        else:
            for day in days_of_work:
                day_times = day[2:]
                day_abbreviation = day[:2]
                day_obj = Day(day_abbreviation)
                day_cost = day_obj.calculate_day_cost(day_times)
                salary += day_cost

        self.salary = salary

        return salary
