import unittest

from exceptions import FileWithBadFormation, HourShiftError
from model.employee import Employee


class TestEmployee(unittest.TestCase):
    def test_employe_creation_with_success(self):
        name: str = 'JOAO'
        days_worked: str = 'MO1:00-10:00,TH4:00-11:00,SA10:00-05:00'
        employee = Employee(name, days_worked)
        assert isinstance(employee, Employee)
        assert hasattr(employee, 'name')
        assert hasattr(employee, 'days_worked')

    def test_employee_calculate_salary_with_success(self):
        name: str = 'JOAO'
        days_worked: str = 'MO1:00-10:00,TH4:00-11:00,SA10:00-15:00'
        employee = Employee(name, days_worked)
        salary = employee.calculate_salary()
        assert salary == 470

    def test_employee_calculate_salary_with_hour_error(self):
        name: str = 'JOAO'
        days_worked: str = 'MO1:00-10:00,TH4:00-11:00,SA17:00-15:00'
        employee = Employee(name, days_worked)
        with self.assertRaises(HourShiftError) as context:
            employee.calculate_salary()
        self.assertTrue('(17, 15)' in str(context.exception))

    def test_employee_calculate_salary_with_bad_formation_error(self):
        name: str = 'JOAO'
        days_worked: str = ''
        employee = Employee(name, days_worked)
        with self.assertRaises(FileWithBadFormation) as context:
            employee.calculate_salary()
        self.assertTrue('Error obtaining datetimes' in str(context.exception))
