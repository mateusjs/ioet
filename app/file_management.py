import os
from typing import List
from exceptions import BlankFile
from model.employee import Employee
from utils import get_name, get_days_of_work, file_path_based_on_os


def find_employee_on_file():
    file = get_file()
    employees = []
    for line in file:
        name: str = get_name(line)
        days_worked: str = get_days_of_work(line)
        employee = Employee(name, days_worked)
        employee.calculate_salary()
        employees.append(employee)
    write_data_to_file(employees)


def get_file() -> str:
    file_path = os.path.join(os.getcwd(), file_path_based_on_os('file.txt'))
    return read_file(file_path)


def read_file(path: str):
    try:
        file_lines = []
        with open(path) as file:
            file_lines = file.readlines()
    except FileNotFoundError:
        raise

    if not file_lines:
        raise BlankFile('File has no content')

    return file_lines


def write_data_to_file(employe_list: List[Employee]):
    dir = os.path.join(
        os.getcwd(), file_path_based_on_os('employees_payment.txt')
    )
    with open(dir, "w") as file:
        lines = []
        for employee in employe_list:
            print(
                f'The amount to pay {employee.name} is: {employee.salary} USD')
            lines.append(f'{employee.name}={employee.days_worked}')
            lines.append(
                f'The amount to pay {employee.name} is: {employee.salary} USD')
        file.write('\n'.join(lines))
