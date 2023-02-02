from typing import List
import os

from exceptions import BlankFile
from model.employee import Employee
from utils import file_path_based_on_os, get_days_of_work, get_name

class EmployeeFileHandler:
    def __init__(self):
        self.employee_file_path = os.path.join(os.getcwd(), file_path_based_on_os('file.txt'))
        self.employee_payment_file_path = os.path.join(os.getcwd(), file_path_based_on_os('employees_payment.txt'))
        self.employees = []

    def find_employee_on_file(self):
        self.read_file()
        self.calculate_employee_salaries()
        self.write_data_to_file()

    def read_file(self):
        try:
            with open(self.employee_file_path) as file:
                file_lines = file.readlines()
        except FileNotFoundError:
            raise

        if not file_lines:
            raise BlankFile('File has no content')

        for line in file_lines:
            name = get_name(line)
            days_worked = get_days_of_work(line)
            employee = Employee(name, days_worked)
            self.employees.append(employee)

    def calculate_employee_salaries(self):
        for employee in self.employees:
            employee.calculate_salary()

    def write_data_to_file(self):
        with open(self.employee_payment_file_path, "w") as file:
            lines = []
            for employee in self.employees:
                print(f'The amount to pay {employee.name} is: {employee.salary} USD')
                lines.append(f'{employee.name}={employee.days_worked}')
                lines.append(f'The amount to pay {employee.name} is: {employee.salary} USD')
            file.write('\n'.join(lines))
