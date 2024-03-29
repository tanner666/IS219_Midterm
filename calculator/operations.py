'''Operations of the calculator'''
from decimal import Decimal
import math

# Functions are defined with type hints (statically typed for better effiency)
def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def log(a: Decimal, base: Decimal = Decimal('10')) -> Decimal:
    """Default log for base 10"""
    if a <= 0:
        raise ValueError("Logarithm undefined for zero or negative numbers")
    if base <= 1:
        raise ValueError("Logarithm undefined for base <= 1")
    return Decimal(math.log(a, float(base)))
