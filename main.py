from operations.division_op import division
from operations.sum_op import sum
from operations.subtraction_op import subtraction
from operations.multiplication_op import multiplication

def user_input():
    print("Operations:")
    print("1. Sum")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("0. Leave\n")

    operation = input("Choose your operation: ")
    if operation == "0":
        print("Finished code")
        return None, None, None

    print()
    n1 = float(input("Type the first number: "))
    n2 = float(input("Type the second number: "))
    return operation, n1, n2

def calculate(operation, n1, n2):
    if operation == "1":
        print("Sum")
        result = sum(n1, n2)
    elif operation == "2":
        print("Subtraction")
        result = subtraction(n1, n2)
    elif operation == "3":
        print("Multiplication")
        result = multiplication(n1, n2)
    elif operation == "4":
        print("Division")
        result = division(n1, n2)
    else:
        print("Invalid Operation.")
        result = None
    return result

if __name__ == "__main__":
    operation, n1, n2 = user_input()
    if operation is not None:
        result = calculate(operation, n1, n2)
        if result is not None:
            print(f"Result: {result}")