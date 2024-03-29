from calculator.commands import Command
from calculator.calculations import Calculations
from calculator.calculation import Calculation
from calculator.commands import Methods  # For high-precision arithmetic
from decimal import Decimal  # For high-precision arithmetic
from calculator.operations import add
from calculator.operations import subtract
from calculator.operations import multiply
from calculator.operations import divide
from calculator.operations import log


class HistoryCommand(Command):
    
    def execute(self, args):
        operation_mapping = {
            'add': add,
            'subtract': subtract,
            'divide': divide,
            'multiply': multiply,
            'log': log
            }
        
        sign_mapping = {
            'add': '+',
            'subtract': '-',
            'divide': '/',
            'multiply': '*',
            'log': 'log'
        }
        # get history
        history = Calculations.get_history()

        # print calculations
        for calculation in history:
            print(f"{calculation[1]} {sign_mapping[calculation[0]]} {calculation[2]} = {Methods._retrieve_result(Decimal(calculation[1]),Decimal(calculation[2]), operation_mapping[calculation[0]])}")
