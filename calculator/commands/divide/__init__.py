from decimal import Decimal  # For high-precision arithmetic
from calculator.operations import divide
from calculator.commands import Command
from calculator.commands import Methods

class DivideCommand(Command):
    def execute(self, args):
        try:
            a, b = map(Decimal, args)
            print(f"The result of {a} / {b} is equal to {Methods._perform_operation(a, b, divide)}")
        except ValueError:
            print("Invalid input. Please enter numbers in the format 'divide a b'.")
