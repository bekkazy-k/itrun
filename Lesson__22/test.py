from .main import Employee, get_employee_by_name, get_employee_by_email, get_employee_by_salary, add_employee
import unittest

class GodDamnTesting(unittest.TestCase):
    emp = Employee()
    def correct(self):
        def Liam(self):
            self.assertEqual(emp.get_employee_by_name('Liam'), emp.employee_list[0])
            self.assertEqual(emp.get_employee_by_email('liam006@gmail.com'), emp.employee_list[2])
            self.assertEqual(emp.get_employee_by_salary(8200), emp.employee_list[4])
        def Oliver(self):
            self.assertEqual(emp.get_employee_by_name('Oliver'), emp.employee_list[0])
            self.assertEqual(emp.get_employee_by_email('mad_oliver@gmail.com'), emp.employee_list[2])
            self.assertEqual(emp.get_employee_by_salary(6150), emp.employee_list[4])
        def William(self):
            self.assertEqual(emp.get_employee_by_name('William'), emp.employee_list[0])
            self.assertEqual(emp.get_employee_by_email('william.jackson@gmail.com'), emp.employee_list[2])
            self.assertEqual(emp.get_employee_by_salary(5550), emp.employee_list[4])
        def Mason(self):
            self.assertEqual(emp.get_employee_by_name('Mason'), emp.employee_list[0])
            self.assertEqual(emp.get_employee_by_email('mason@gmail.com'), emp.employee_list[2])
            self.assertEqual(emp.get_employee_by_salary(5300), emp.employee_list[4])

    def have_not(self):
        self.assertEqual(emp.get_employee_by_name('wrong name'), False)
        self.assertEqual(emp.get_employee_by_email('wrong mail'), False)
        self.assertEqual(emp.get_employee_by_salary(0000), False)

    def uncorrect(self):
        self.assertEqual(emp.get_employee_by_name(False), False)
        self.assertEqual(emp.get_employee_by_email('sobakamail'), False)
        self.assertEqual(emp.get_employee_by_salary([{'salary': 0000}]), False)

    def try_add(self):
        def correct_add(self):
            emp.add_employee('Alex', '88005553535', 'alexvance@gmail.com', 'developer', 7580)
            res = {
                "name": "Alex",
                "phone": "88005553535",
                "email": "alexvance@gmail.com",
                "position": "developer",
                "salary": 7580
            }
            self.assertEqual(emp.get_employee_by_name('Alex'), res)
        def wrong_add(self):
            emp.add_employee(True, 88005553535, ['alexvance@gmail.com'], {'developer'}, '7580')
            self.assertEqual(emp.get_employee_by_name(True), False)
