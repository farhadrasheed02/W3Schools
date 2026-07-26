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

def factorial(n):
    """Recursion function is when a function is calling itself in the same
    function factorial function is a prime example of this behaviour."""
    if n ==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)

def Fibonacci(n):
    if n ==1:
        return n
    elif n==0:
        return 0
    return Fibonacci(n-1) + Fibonacci(n-2)




