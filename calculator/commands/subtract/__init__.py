from decimal import Decimal  # For high-precision arithmetic
from calculator.operations import subtract
from calculator.commands import Command
from calculator.commands import Methods
from calculator.calculations import Calculations


class SubtractCommand(Command):
    def execute(self, args):
        try:
            a, b = map(Decimal, args)
            print(f"The result of {a} - {b} is equal to {Methods._perform_operation(a, b, subtract)}")
        except ValueError:
            print("Invalid input. Please enter numbers in the format 'subtract a b'.")
