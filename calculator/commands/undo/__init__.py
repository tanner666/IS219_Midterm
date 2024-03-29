from calculator.commands import Command
from calculator.calculations import Calculations

class ClearHistoryCommand(Command):
    def execute(self, args):
        # clear history
        Calculations.remove_latest()

        print("Removed last calculation successfully!")
        