from decimal import Decimal
from calculator.commands import Methods  # For high-precision arithmetic
from calculator.operations import add
from calculator.commands import Command
from calculator.calculations import Calculations


class AddCommand(Command):
    def execute(self, args):
        try:
            a, b = map(Decimal, args)
            print(f"The result of {a} + {b} is equal to {Methods._perform_operation(a, b, add)}")
        except ValueError:
            print("Invalid input. Please enter numbers in the format 'add a b'.")
