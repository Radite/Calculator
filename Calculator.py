import math
def add(x,y):
    return x+y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y
    
def sqrt(x):
    return math.sqrt(x)

def square(x):
    return x**2

def inverse(x):
    return 1/x

def mod(x,y):
    return x-((x//y)*y)

def factorial(x):
    result = 1
    for i in range(1, x+1):
        result*=i
    return result

def exp(x,y):
    return x*(10**y)

def calculate_log(x, base):
    if x <= 0:
        raise ValueError("Logarithm is not defined for non-positive values.")
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1.")
    return math.log(x, base)  # Logarithm to the specified base

def calculate_ln(x):
    if x <= 0:
        raise ValueError("The natural logarithm is not defined for non-positive values.")
    return math.log(x)  # Defaults to the natural logarithm (base e)

def exp10(x):
    return 10**x

def power(x,y):
    return x**y

def yth_root_of_x(x, y):
    # Ensure that we don't attempt to take the root of a negative number when y is even,
    # as this would result in a complex number which math.pow can't handle.
    if x < 0 and y % 2 == 0:
        raise ValueError("Cannot take an even root of a negative number.")
    return math.pow(x, 1/y)

def get_input():
    calc = input("Enter type of calculator needed: Standard or Scientific: ").strip().lower()
    if calc == "standard":
        operation = input("Enter operation (add, subtract, multiply, divide): ").strip()
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return operation, num1, num2
    elif calc == "scientific":
        # Get the operation from the user
        operation = input("Enter operation (add, subtract, multiply, divide, sqrt, square, inverse, mod, factorial, exp, log, ln, exp10, power, root): ").strip().lower()

        # Operations that require only one input
        unary_operations = ['sqrt', 'square', 'inverse', 'factorial', 'ln', 'exp10']

        # Check if the operation is unary and request only one number if so
        if operation in unary_operations:
            num1 = float(input("Enter the number: "))
            return operation, num1, None  # No second number needed for unary operations

        # For binary operations, get two numbers
        else:
            num1 = float(input("Enter the first number: "))
            # For operations that require a second number, request it
            if operation in ['add', 'subtract', 'multiply', 'divide', 'mod', 'exp', 'log', 'power', 'root']:
                num2 = float(input("Enter the second number: "))
            else:
                print("Invalid operation or operation not supported.")
                return None, None, None  # Invalid operation

        return operation, num1, num2
    else:
        return "Invalid calculator chosen"

def main():
    while True:
        operation, num1, num2 = get_input()

        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        elif operation == "sqrt":
    # Calculate the square root of the first number
            result = sqrt(num1)
        elif operation == "square":
            # Calculate the square of the first number
            result = square(num1)
        elif operation == "inverse":
            # Calculate the inverse of the first number
            result = inverse(num1)
        elif operation == "mod":
            # Calculate the modulus of the first number by the second number
            result = mod(num1, num2)
        elif operation == "factorial":
            # Calculate the factorial of the first number
            result = factorial(int(num1))  # Cast to int in case of non-integer input
        elif operation == "exp":
            # Calculate the exponent of the first number by the power of 10 to the second number
            result = exp(num1, num2)
        elif operation == "log":
            # Calculate the logarithm of the first number with the second number as the base
            result = calculate_log(num1, num2)
        elif operation == "ln":
            # Calculate the natural logarithm of the first number
            result = calculate_ln(num1)
        elif operation == "exp10":
            # Calculate 10 raised to the power of the first number
            result = exp10(num1)
        elif operation == "power":
            # Calculate the first number raised to the power of the second number
            result = power(num1, num2)
        elif operation == "root":
            # Calculate the y-th root of x (first number is x, second number is y)
            result = yth_root_of_x(num1, num2)
        else:
            print("Invalid operation")
            continue

        print("The result is", result)

        if input("\nDo you want to perform another calculation? (yes/no): ").strip().lower() != 'yes':
            break

if __name__ == "__main__":
    main()