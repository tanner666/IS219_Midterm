'''
    This code snippet demonstrates how to define a class in Python that 
    encapsulates a mathematical calculation, including two operands (a and b) 
    and an operation (like add or subtract). 
    The operation parameter is a higher-order function, meaning it takes 
    functions as arguments or returns them. 
    This approach leverages Python's first-class functions to create 4
    flexible and reusable code. The use of Decimal from the decimal 
    module instead of floating-point numbers is crucial for 
    financial and scientific calculations that require high precision. 
    The __repr__ method provides a developer-friendly string representation 
    of the object, useful for debugging and logging.
'''
from decimal import Decimal
from typing import Callable, Optional, Union #type hints for functions

# Calculations can be performed on both one and two operand operations
class Calculation:
    def __init__(self, a: Decimal, operation: Union[Callable[[Decimal], Decimal], Callable[[Decimal, Decimal], Decimal]], b: Optional[Decimal] = None):
        """Constructor, with either one or two operands. b = None if nothing entered"""
        self.a = a
        self.b = b
        self.operation = operation #function

    # Static method to create a new instance of Calculation
    # This method provides an alternative constructor that can be used without instantiating the class directly
    @staticmethod
    def create(a: Decimal, operation: Union[Callable[[Decimal], Decimal], Callable[[Decimal, Decimal], Decimal]], b: Optional[Decimal] = None):
        """Return a new calculation object, intialized with provided arguments"""
        return Calculation(a, operation, b)
    
    
    # Method to perform the calculation stored in this object
    def perform_one_operand(self) -> Decimal:
        """Perform the stored calculation on one operand and return the result."""
        return self.operation(self.a)
    
    # Method to perform the calculation stored in this object
    def perform_two_operands(self) -> Decimal:
        """Perform the stored calculation on two operands and return the result."""
        return self.operation(self.a, self.b)
    
    # Uses an f-string (formattted string) to embed expressions inside of a string (like printf() in C)
    def __repr__(self):
        """Return a simplified string representation of the calculation"""
        b_repr = f", {self.b}" if self.b is not None else ""
        return f"Calculation({self.a}, {self.operation.__name__}{b_repr})"
    