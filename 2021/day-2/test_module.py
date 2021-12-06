import unittest
from day_2 import (
    return_product_of_distance_and_depth,
    return_product_of_distance_and_depth_including_aim
)


class UnitTests(unittest.TestCase):

    def test_return_product_of_distance_and_depth_with_provided_input(self):
        actual_output = return_product_of_distance_and_depth()
        expected_output = 1727835
        self.assertEqual(actual_output, expected_output,
                         'Expected calling `return_product_of_distance_and_depth() with the provided input to return 1727835.')

    def test_return_product_of_distance_and_depth_outputs_an_integer(self):
        actual_output_type = type(return_product_of_distance_and_depth())
        expected_output_type = int
        self.assertEqual(actual_output_type, expected_output_type,
                         'Expected `return_product_of_distance_and_depth()` to return a value of type int.')

    def test_return_product_of_distance_and_depth_including_aim_with_provided_input(self):
        actual_output = return_product_of_distance_and_depth_including_aim()
        expected_output = 1544000595
        self.assertEqual(actual_output, expected_output,
                         'Expected calling `find_count_of_slide_window_increases() with the provided INPUT list to return 1600.')

    def test_return_product_of_distance_and_depth_including_aim_outputs_an_integer(self):
        actual_output_type = type(
            return_product_of_distance_and_depth_including_aim())
        expected_output_type = int
        self.assertEqual(actual_output_type, expected_output_type,
                         'Expected `return_product_of_distance_and_depth_including_aim()` to return a value of type int.')


if __name__ == "__main__":
    unittest.main()
