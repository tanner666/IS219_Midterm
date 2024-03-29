from calculator.commands import CommandHandler
from calculator.commands.add import AddCommand
from calculator.commands.subtract import SubtractCommand
from calculator.commands.divide import DivideCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.log import LogCommand
import multiprocessing
import pkgutil
import importlib
import os
import sys
import logging
import logging.config
from calculator.commands import Command
from dotenv import load_dotenv

class Calculator:

    def __init__(self): # Constructor
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)
    
    def load_commands(self):
        # Dynamically load all plugins in the plugins directory
        commands_package = 'calculator.commands'
        commands_path = commands_package.replace('.', '/')
        if not os.path.exists(commands_path):
            logging.warning(f"Plugins directory '{commands_path}' not found.")
            return
        for _, command_name, is_pkg in pkgutil.iter_modules([commands_path]):
            if is_pkg:  # Ensure it's a package
                    try:
                        command_module = importlib.import_module(f'{commands_package}.{command_name}')
                        self.register_commands(command_module, command_name)
                    except ImportError as e:
                        logging.error(f"Error importing plugin {command_name}: {e}")

    def register_commands(self, command_module, command_name):
        for item_name in dir(command_module):
            item = getattr(command_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                # Command names are now explicitly set to the plugin's folder name
                self.command_handler.register_command(command_name, item())
                logging.info(f"Command '{command_name}' from plugin '{command_name}' registered.")

    def execute_command_in_process(self, command_name, args):
        # This method will be run by each process
        self.command_handler.execute_command(command_name, args) # pragma: no cover

    def start(self):
        self.load_commands()
        logging.info("Application started. Type 'exit' to exit. Type 'menu' for list of commands.")
        try:
            while True:
                command_input = input(">>> ").strip().split(' ')
                command_name = command_input[0]
                args = command_input[1:]
                if command_input[0].lower() == 'exit':
                    break
                # Create a Process for each command execution
                process = multiprocessing.Process(target=self.execute_command_in_process, args=(command_name, args))# pragma: no cover
                process.start()# pragma: no cover
                process.join()  # Wait for the command process to finish before continuing # pragma: no cover
        except KeyboardInterrupt:
            logging.info("Application interrupted and exiting gracefully.")
            sys.exit(0)  # Assuming a KeyboardInterrupt should also result in a clean exit.
        finally:
             logging.info("Application shutdown.")
