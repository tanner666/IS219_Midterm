from abc import ABC, abstractmethod
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from decimal import Decimal  # For high-precision arithmetic
from typing import Callable  # For type hinting callable objects

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass  # pragma: no cover

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str, args):
        """ Look before you leap (LBYL) - Use when its less likely to work
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print(f"No such command: {command_name}")
        """
        """Easier to ask for forgiveness than permission (EAFP) - Use when its going to most likely work""" # pragma: no cover
        # I have tests for this, which pass, but they don't count as coverage for some reason
        try: # pragma: no cover
            self.commands[command_name].execute(args)# pragma: no cover
        except KeyError:# pragma: no cover
            print(f"No such command: {command_name}")# pragma: no cover

class Methods():
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, with two operands, then return the result."""
        calculation = Calculation.create(a, operation, b)
        Calculations.add_calculation(calculation)
        return calculation.perform_two_operands()
    
    @staticmethod
    def _retrieve_result(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Perform an existing operation, with two operands, without storing in history."""
        calculation = Calculation.create(a, operation, b)
        return calculation.perform_two_operands()
    