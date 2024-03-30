'''Operations of the calculator'''
from decimal import Decimal
import math
import logging

# Functions are defined with type hints (statically typed for better effiency)
def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    try:
        return a/b
    except ZeroDivisionError:
        logging.warning("Cannot divide by zero")
        return None

def log(a: Decimal, base: Decimal = Decimal('10')) -> Decimal:
    """Default log for base 10"""
    if a <= 0:
        logging.warning("Logarithm undefined for zero or negative numbers")
        return None
    if base <= 1:
        logging.warning("Logarithm undefined for base <= 1")
        return None
    return Decimal(math.log(a, float(base)))
