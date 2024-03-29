from calculator.commands import Command
from calculator.calculations import Calculations

class ClearHistoryCommand(Command):
    def execute(self, args):
        # clear history
        Calculations.clear_history()

        print("History successfully cleared!")
        