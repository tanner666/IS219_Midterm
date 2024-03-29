from decimal import Decimal  # For high-precision arithmetic
from calculator.operations import log
from calculator.commands import Command
from calculator.commands import Methods

class LogCommand(Command):
    def execute(self, args):
        try:
            a, b = map(Decimal, args)
            print(f"The result of log {a} ({b}) is equal to {Methods._perform_operation(b, a, log)}")
        except ValueError:
            print("Invalid input. Please enter numbers in the format 'log base a'.")
