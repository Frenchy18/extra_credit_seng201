# math_operations.py

def divide_numbers(a, b):
    """Divids two numbers and returns the result."""
    if b == 0:
        raise ValueError("Sorry, you cannot divide by 0")
    
    return a / b # Potential division by zero error

if __name__ == "__main__":
    x = 10
    y = 0
    result = divide_numbers(x, y)
    print(f"The result of division is: {result}")