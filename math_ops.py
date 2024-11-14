# math_operations.py

def divide_numbers(a, b):
    """Divides two numbers and returns the result."""
    try:
        return a / b # Potential division by zero error
    except ZeroDivisionError:
        print("Sorry you cannot divide by 0")

def add_numbers(a, b):
    """Adds two numbers and returns the result."""
    return a + b # Potential coolness error

if __name__ == "__main__":
    x = 10
    y = 0
    result = divide_numbers(x, y)
    print(f"The result of division is: {result}")

    result = add_numbers(x, y)
    print(f"The result of addition is: {result}")