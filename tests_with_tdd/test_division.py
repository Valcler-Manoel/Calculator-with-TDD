import unittest
from operations.division_op import division

class Test_Division(unittest.TestCase):

    def test_divide_with_decimal_numbers_result(self):
        # Arrange
        n1 = 8.5
        n2 = 3.2

        # Act
        result = division(n1, n2)

        # Assert
        self.assertEqual(result, 2.65625)

    def test_divide_negative_numbers_result(self):
        # Arrange
        n1 = -5.0
        n2 = 25.0

        # Act
        result = division(n1, n2)

        # Assert
        self.assertEqual(result, -0.2)

    def test_divide_with_zero_result(self):
        # Arrange
        n1 = 5.0
        n2 = 0.0

        # Act
        result = division(n1, n2)

        # Assert
        self.assertIsNone(result, None)

    def test_division_operation_with_natural_values(self):
        # Arrange
        x = range(0, 101)
        y = range(1, 102)

        # Act
        for n1, n2 in zip(x, y):
            with self.subTest(n1=n1, n2=n2):
                result = division(n1, n2)
                expected_result = n1 / n2
        # Assert
        self.assertEqual(result, expected_result)
