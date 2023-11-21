import unittest
from operations.sum_op import sum

class Test_Sum(unittest.TestCase):

    def test_sum_decimal_numbers_result(self):
        # Arrange
        n1 = 24.8
        n2 = 8.8

        # Act
        result = sum(n1, n2)

        # Assert
        self.assertEqual(result, 33.6)

    def test_sum_negative_numbers_result(self):
        # Arrange
        n1 = -42.0
        n2 = 9.0

        # Act
        result = sum(n1, n2)

        # Assert
        self.assertEqual(result, -33)

    def test_sum_with_zero_result(self):
        # Arrange
        n1 = 77.0
        n2 = 0.0

        # Act
        result = sum(n1, n2)

        # Assert
        self.assertEqual(result, 77)

    def test_sum_operation_with_natural_values(self):
        # Arrange
        x = range(0, 101)
        y = range(0, 101)

        # Act
        for n1, n2 in zip(x, y):
            with self.subTest(n1=n1, n2=n2):
                result = sum(n1, n2)
                expected_result = n1 + n2
        # Assert
                self.assertEqual(result, expected_result)