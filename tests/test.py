from src import main
from unittest.mock import patch, MagicMock
import unittest


class MyTestCase(unittest.TestCase):

    @patch('src.main.add')
    def test_add(self, mock):
        mock.return_value = MagicMock(status_code=200, response=9)
        response = main.add(5, 4)
        self.assertEqual(response.response, 9)

    @patch('src.main.subtract')
    def test_subtract(self, mock):
        mock.return_value = MagicMock(status_code=200, response=1)
        response = main.subtract(5, 4)
        self.assertEqual(response.response, 1)

    @patch('src.main.multiply')
    def test_multiply(self, mock):
        mock.return_value = MagicMock(status_code=200, response=18)
        response = main.multiply(6, 3)
        self.assertEqual(response.response, 18)

    @patch('src.main.divide')
    def test_divide(self, mock):
        mock.return_value = MagicMock(status_code=200, response=3.0)
        response = main.divide(6, 2)
        self.assertEqual(response.response, 3.0)

    @patch('builtins.input', side_effect=[5, 4, 'no'])
    @patch('src.main.add')
    def test_calc_add(self, mock, mock2):
        mock.return_value = 9
        self.assertEqual(main.calc('1'), '5 + 4 = 9')

    @patch('builtins.input', side_effect=[5, 4, 'no'])
    @patch('src.main.subtract')
    def test_calc_subtract(self, mock, mock2):
        mock.return_value = 1
        self.assertEqual(main.calc('2'), '5 - 4 = 1')

    @patch('builtins.input', side_effect=[6, 3, 'no'])
    @patch('src.main.multiply')
    def test_calc_multiply(self, mock, mock2):
        mock.return_value = 18
        self.assertEqual(main.calc('3'), '6 * 3 = 18')

    @patch('builtins.input', side_effect=[6, 2, 'no'])
    @patch('src.main.divide')
    def test_calc_divide(self, mock, mock2):
        mock.return_value = 3.0
        self.assertEqual(main.calc('4'), '6 / 2 = 3.0')

    @patch('builtins.input', side_effect=[5, 'no'])
    def test_calc_invalid(self, mock):
        self.assertEqual(main.calc(5), 'Invalid Input')

    @patch('builtins.input', side_effect=[5, 'no'])
    def test_main_no(self, mock):
        self.assertEqual(main.main(), None)


if __name__ == '__main__':
    unittest.main()
