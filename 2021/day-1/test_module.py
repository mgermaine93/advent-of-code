import unittest
from input import INPUT
from day_1 import (
    find_count_measurement_increases,
    find_count_of_slide_window_increases
)


class UnitTests(unittest.TestCase):

    def test_find_count_measurement_increases_with_provided_input(self):
        actual_output = find_count_measurement_increases(INPUT)
        expected_output = 1559
        self.assertEqual(actual_output, expected_output,
                         'Expected calling `find_count_measurement_increases() with the provided INPUT list to return 1559.')

    def test_find_count_measurement_increases_outputs_an_integer(self):
        actual_output_type = type(find_count_measurement_increases(INPUT))
        expected_output_type = int
        self.assertEqual(actual_output_type, expected_output_type,
                         'Expected `find_count_measurement_increases()` to return a value of type int.')

    def test_find_count_of_slide_window_increases_with_provided_input(self):
        actual_output = find_count_of_slide_window_increases(INPUT)
        expected_output = 1600
        self.assertEqual(actual_output, expected_output,
                         'Expected calling `find_count_of_slide_window_increases() with the provided INPUT list to return 1600.')

    def test_find_count_of_slide_window_increases_outputs_an_integer(self):
        actual_output_type = type(find_count_of_slide_window_increases(INPUT))
        expected_output_type = int
        self.assertEqual(actual_output_type, expected_output_type,
                         'Expected `find_count_of_slide_window_increases()` to return a value of type int.')


if __name__ == "__main__":
    unittest.main()
