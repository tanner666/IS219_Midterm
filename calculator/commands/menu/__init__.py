from calculator.commands import Command
import os

class MenuCommand(Command):
    def execute(self, args):
        # Define the path to your commands directory
        commands_directory = "calculator/commands"

        # Get a list of all items in the commands directory
        commands_list = os.listdir(commands_directory)

        # Filter out the menu command directory (assuming its name is 'menu')
        commands_list = [cmd for cmd in commands_list if cmd != 'menu' and cmd != '__pycache__' and cmd != '__init__.py']

        # Print the names of the command directories
        for command_name in commands_list:
            print(command_name)
