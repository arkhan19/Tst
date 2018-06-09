import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('Abdul', 'Khan', 50000)
        emp_2 = Employee('dARK', 'f3n1Xx', 60000)

        self.assertEqual(emp_1.email, 'Abdul.Khan@email.com')
        self.assertEqual(emp_2.email, 'dARK.f3n1Xx@email.com')

        emp_1.first = 'Jon'
        emp_2.first = 'Kon'

        self.assertEqual(emp_1.email, 'Jon.Khan@email.com')
        self.assertEqual(emp_2.email, 'Kon.f3n1Xx@email.com')

    def test_fullname(self):
        emp_1 = Employee('Abdul', 'Khan', 50000)
        emp_2 = Employee('dARK', 'f3n1Xx', 60000)

        self.assertEqual(emp_1.fullname, 'Abdul Khan')
        self.assertEqual(emp_2.fullname, 'dARK f3n1Xx')

        emp_1.first = 'Jon'
        emp_2.first = 'Kon'

        self.assertEqual(emp_1.fullname, 'Jon Khan')
        self.assertEqual(emp_2.fullname, 'Kon f3n1Xx')

    def test_apply_raise(self):
        emp_1 = Employee('Abdul', 'Khan', 50000)
        emp_2 = Employee('dARK', 'f3n1Xx', 60000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()
