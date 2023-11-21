import unittest
from operations.subtraction_op import subtraction

class Test_Subtraction(unittest.TestCase):

    def test_subtract_decimal_numbers_result(self):
        # Arrange
        n1 = 9.2
        n2 = 5.8

        # Act
        result = subtraction(n1, n2)

        # Assert
        self.assertEqual(result, 3.4)

    def test_subtract_negative_numbers_result(self):
        # Arrange
        n1 = -18.0
        n2 = 2.0

        # Act
        result = subtraction(n1, n2)

        # Assert
        self.assertEqual(result, -20)

    def test_multiplication_with_zero_result(self):
        # Arrange
        n1 = 5.0
        n2 = 0.0

        # Act
        result = subtraction(n1, n2)

        # Assert
        self.assertEqual(result, 5)

    def test_subtration_operation_with_natural_values(self):
        # Arrange
        x = range(0, 101)
        y = range(0, 101)

        # Act
        for n1, n2 in zip(x, y):
            with self.subTest(n1=n1, n2=n2):
                result = subtraction(n1, n2)
                expected_result = n1 - n2
        # Assert
                self.assertEqual(result, expected_result)