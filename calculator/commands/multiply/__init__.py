from decimal import Decimal  # For high-precision arithmetic
from calculator.operations import multiply
from calculator.commands import Command
from calculator.commands import Methods

class MultiplyCommand(Command):
    def execute(self, args):
        try:
            a, b = map(Decimal, args)
            print(f"The result of {a} * {b} is equal to {Methods._perform_operation(a, b, multiply)}")
        except ValueError:
            print("Invalid input. Please enter numbers in the format 'multiply a b'.")
