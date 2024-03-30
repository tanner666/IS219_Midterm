# IS219_Midterm

[Demo Video](https://youtu.be/ENCo4s-fEqg)

## Documentation

You must have git and Python installed to run this.

### How to test it out

- navigate to local directory you want to run project in and run: $git clone <repository-url>
- install dependencies with: $pip install -r requirements.txt
- run the code: $python main.py   (or python3 main.py)
- type 'menu' to see a full list of commands you can execute

## Design Patterns

### Strategy Pattern

This pattern revolves around encapsulating algorithms/strategies in separate classes/functions, to make them interchangeable with a context object. The main way I implemented this was through the 'operation' parameter that is passed to the Calculation class, allowing any one of five different operations to be passed all in a single call. ex: 

    class Calculation:
        def __init__(self, a: Decimal, operation: Union[Callable[[Decimal], Decimal], Callable[[Decimal, Decimal], Decimal]], b: Optional[Decimal] = None):
            """Constructor, with either one or two operands. b = None if nothing entered"""
            self.a = a
            self.b = b
            self.operation = operation #function

### Singleton

Singleton is a pattern in which a class is designed to operate without creating instances of itself, to ensure all interactions with it are centralized through a single access point. My calculations.py class uses this approach, since all of the methods are class methods which manipulate the shared resource of the history.csv file.

    def __new__(cls):
        raise NotImplementedError("This class cannot be instantiated")

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the calculator history file"""
       ...
       
    @classmethod
    def get_history(cls) -> List[List[str]]:


### Facade Pattern

The Facade pattern provides a unified/simplified interface (or facade class) that hides the complexities of the underlying classes/frameworks. The main way I implemented this was by having my main.py file act as a simple entry point into the program, which then called the more complex methods and REPL loop hidden in the Calculation class. ex: 

main.py

    from calculator import Calculator    
    
    if __name__ == "__main__":
        calculator = Calculator().start()  # Instantiate an instance of App

Calculator

    class Calculator:

        def __init__(self): # Constructor
            os.makedirs('logs', exist_ok=True)
            self.configure_logging()
            load_dotenv()
            self.settings = self.load_environment_variables()
            self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
            self.command_handler = CommandHandler()

    def configure_logging(self):
        ...

    def load_environment_variables(self):
       ...

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        ...
    
    def load_commands(self):
        ...

    def register_commands(self, command_module, command_name):
        ...

    def execute_command_in_process(self, command_name, args):
        ...

    def start(self):
        ...
        try:
            while True:
                command_input = input(">>> ").strip().split(' ')
                command_name = command_input[0]
                args = command_input[1:]
                if command_input[0].lower() == 'exit':
                    break
                # Create a Process for each command execution
        ...


### Command Pattern

This pattern encapsulates all information needed to perform an action (like method call, parameters, obecjects, etc) in commands. It also uses a CommandHandler to call the Commands to process requests. ex from my calculator and commands __init__ files: 

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
            ...
            
### Factory Method

This pattern provides an interface for creating objects or generating data, while allowing the type of objects created to be altered. This is most apparent in my conftest.py file, where I use the Faker library to create a substantial amount of fake data to test my calculator on: 

    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        # use first Decimal() if _ % 4 != 3, else use second Decimal()
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        # Randomly obtain operation_name from map
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]
        ...
        performing the operations on the fake data ...

### REPL

Implemented a Read-Eval-Print Loop (REPL) to facilitate direct interaction with the calculator. 
- main.py is entry point and calls Calculator().start()
- this start command loads all plugins and starts a loop
- the loop keeps running and accepting input until a keyboard interrupt or exit is entered

## Environment Variables

Env variables are stored in .env file (not uploaded to github), and are used to enhance the configurability, security, and usability of a program. They are often used to configure local environments, set modes, set usernames/passwords, and store api keys. In this project, the path to the csv file could be set as an environment variable and used within the program, so that it is easily configurable. However, I just hardcoded the path for the sake of this project. 

Despite not utilizing them here, the Calculator class includes robust methods for dynamically loading and retrieving environment variables at the start of the program, in case they would ever be used in the future. These methods are located in the calculator/__init__.py file

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

## Logging

Established a comprehensive logging system, throughout the entirety of the project, to record current states of the program:
- **Note, usually this isn't uploaded to github, but for the sake of the midterm demo, I have uploaded the log file under the /logs folder
- info logs are recored whenever a change occurs within the program (app starting, commands registering, app exiting, etc)
- warning logs are recorded whenever a mistake occurs, like the user trying to divide by zero, or file not being found
- error logs are recorded whenever a fatal problem occurs, such as a plugin not importing correctly

## Try/Except + LBYL + EAFP

Try/Except structures align with the EAFP approach, in which you attempt to execute code and catch any exceptions that arise when you execute it. This is extremely useful in scenarios where you are expecting an exception sometimes and want to specify how you handle it. One of the best examples of this is with division and divide by zero error (from my code):

    def divide(a: Decimal, b: Decimal) -> Decimal:
      try:
          return a/b
      except ZeroDivisionError:
          logging.warning("Cannot divide by zero")
          return None

The Look Before You Leap is a more careful approach, used to look for potential issues/errors before you even execute the code. An example of how I used this is at the start of my program, where it's crucial to have the plugins (commands) directory exist: 

    if not os.path.exists(commands_path):
      logging.warning(f"Plugins directory '{commands_path}' not found.")
            return

I also use both of these structures throughout the program, whenever I know that a potential issue could arise with the code that I need to check for. Try/Except are generally used in less costly areas, or when a specific issue might arise. LBYL is generally a safer approach, used in more costly situations where you can't continue if a condition fails.
          

### Plugin System

Created a flexible plugin system to allow seamless integration of new commands or features. 
- the commands folder contains plugins, or commands, the user can enter
- these commands are registered and loaded into the program at the start
- menu command allows users to view a list of all commands

## Calculation History Management with Pandas

Utilized Pandas to manage a robust calculation history:
- calculations.py file defines methods for adding, saving, removing, clearing, and retrieving the history.csv file
- calculations are loaded into a pandas dataframe, stored in the csv file as strings (op, a, b), and reconverted back into calculations when the history is retrieved
- data can also be manipulated, such as undoing last operation

