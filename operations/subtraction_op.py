def subtraction(n1: float, n2: float, precision: int = 10) -> float:
    """Compute and return the difference of two given numbers.

    Args:
        n1 (float): The first number
        n2 (float): The second number
    """
    result = n1 - n2

    rounded_result = round(result, precision)

    return rounded_result