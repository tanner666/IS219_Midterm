# IS219_Midterm

[Demo Video](https://youtu.be/ENCo4s-fEqg)

## Documentation

You must have git and Python installed to run this.

### How to test it out

- navigate to local directory you want to run project in and run: git clone <repository-url>
- install dependencies with: pip install -r requirements.txt
- run the code: python main.py   (or python3 main.py)
- type 'menu' to see a full list of commands you can execute

## Design Patterns

### Facade Pattern

### Command Pattern

### Factory Method

### REPL

## Environment Variables

Env variables are stored in .env file (not uploaded to github), and are used to enhance the configurability, security, and usability of a program. They are often used to configure local environments, set modes, set usernames/passwords, and store api keys. In this project, the path to the csv file could be set as an environment variable and used within the program, so that it is easily configurable. However, I just hardcoded the path for the sake of this project. 

Despite not utilizing them here, the Calculator class includes robust methods for dynamically loading and retrieving environment variables at the start of the program, in case they would ever be used in the future. These methods are located in the calculator/__init__.py file

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
          


### Command-Line Interface (REPL)

Implemented a Read-Eval-Print Loop (REPL) to facilitate direct interaction with the calculator. 
- main.py is entry point and calls Calculator().start()
- this start command loads all plugins and starts a loop
- the loop keeps running and accepting input until a keyboard interrupt or exit is entered

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

