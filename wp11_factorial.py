import math

def factorial(n):
    if not isinstance(n, int):
        raise ValueError("Argument is not int!")
    elif n < 0:
        raise ValueError("Not a positive integer!")
    else: return math.factorial(n)
    
print(factorial(2))
