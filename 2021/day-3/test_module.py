import unittest
from day_3 import (
    find_gamma_rate,
    find_epsilon_rate,
    find_power_consumption
)


class UnitTests(unittest.TestCase):

    def test_find_gamma_rate_with_provided_input(self):
        actual_output = find_gamma_rate()
        expected_output = 110111001001
        self.assertEqual(actual_output, expected_output,
                         'Expected calling `find_gamma_rate()` with the provided input to return 110111001001.')

    def test_find_gamma_rate_returns_a_string(self):
        actual_output_type = type(find_gamma_rate())
        expected_output_type = str
        self.assertEqual(actual_output_type, expected_output_type,
                         'Expected `find_gamma_rate()` to return a value of type str.')

    def test_find_epsilon_rate_with_provided_input(self):
        actual_output = find_epsilon_rate()
        expected_output = int("001000110110")
        self.assertEqual(actual_output, expected_output,
                         'Expected calling `find_gepsilon_rate()` with the provided input to return 001000110110.')

    def test_find_epsilon_rate_returns_a_string(self):
        actual_output_type = type(find_epsilon_rate())
        expected_output_type = str
        self.assertEqual(actual_output_type, expected_output_type,
                         'Expected `find_epsilon_rate()` to return a value of type str.')

    def test_find_power_consumption_with_provided_input(self):
        actual_output = find_power_consumption()
        expected_output = 1997414
        self.assertEqual(actual_output, expected_output,
                         'Expected calling `find_power_consumption()` with the provided input to return 1997414.')

    def test_find_epsilon_rate_returns_an_int(self):
        actual_output_type = type(find_power_consumption())
        expected_output_type = int
        self.assertEqual(actual_output_type, expected_output_type,
                         'Expected `find_power_consumption()` to return a value of type int.')


if __name__ == "__main__":
    unittest.main()
