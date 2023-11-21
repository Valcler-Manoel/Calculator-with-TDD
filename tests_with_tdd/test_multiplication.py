import unittest
from operations.multiplication_op import multiplication

class Test_Multiplication(unittest.TestCase):

    def test_multiply_decimal_numbers_result(self):
        # Arrange
        n1 = 5.5
        n2 = 3.2

        # Act
        result = multiplication(n1, n2)

        # Assert
        self.assertEqual(result, 17.6)

    def test_multiply_negative_numbers_result(self):
        # Arrange
        n1 = -2.0
        n2 = 4.0

        # Act
        result = multiplication(n1, n2)

        # Assert
        self.assertEqual(result, -8.0)

    def test_multiplication_with_zero_result(self):
        # Arrange
        n1 = 5.0
        n2 = 0.0

        # Act
        result = multiplication(n1, n2)

        # Assert
        self.assertEqual(result, 0.0)

    def test_multiplication_operation_with_natural_values(self):
        # Arrange
        x = range(0, 101)
        y = range(0, 101)

        # Act
        for n1, n2 in zip(x, y):
            with self.subTest(n1=n1, n2=n2):
                result = multiplication(n1, n2)
                expected_result = n1 * n2
        # Assert
                self.assertEqual(result, expected_result)