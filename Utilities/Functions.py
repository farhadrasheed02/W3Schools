def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a // b

def square(n):
    """
    This function takes an argument and returns square of it. Note: The statement written b/w triple quotes is called doc string.
    doc string is always written just after the function name and before the function definition gets implemented...
    """
    return n*n