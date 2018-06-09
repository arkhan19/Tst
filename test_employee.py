import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass\n')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass\n')

    def setUp(self):
        self.emp_1 = Employee('Abdul', 'Khan', 50000)
        self.emp_2 = Employee('dARK', 'f3n1Xx', 60000)
        print('setUp\n')

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Abdul.Khan@email.com')
        self.assertEqual(self.emp_2.email, 'dARK.f3n1Xx@email.com')

        self.emp_1.first = 'Jon'
        self.emp_2.first = 'Kon'

        self.assertEqual(self.emp_1.email, 'Jon.Khan@email.com')
        self.assertEqual(self.emp_2.email, 'Kon.f3n1Xx@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Abdul Khan')
        self.assertEqual(self.emp_2.fullname, 'dARK f3n1Xx')
        self.emp_1.first = 'Jon'
        self.emp_2.first = 'Kon'

        self.assertEqual(self.emp_1.fullname, 'Jon Khan')
        self.assertEqual(self.emp_2.fullname, 'Kon f3n1Xx')

    def test_apply_raise(self):

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.gg/Khan/June')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False
            mocked_get.return_value.text = 'Failed'

            schedule = self.emp_2.monthly_schedule('April')
            mocked_get.assert_called_with('http://company.gg/f3n1Xx/April')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
