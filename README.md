# IS219_Midterm
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

### Calculation History Management with Pandas

Utilized Pandas to manage a robust calculation history:
- calculations.py file defines methods for adding, saving, removing, clearing, and retrieving the history.csv file
- calculations are loaded into a pandas dataframe, stored in the csv file as strings (op, a, b), and reconverted back into calculations when the history is retrieved
- data can also be manipulated, such as undoing last operation


### Professional Logging Practices

Established a comprehensive logging system:
- **Note, usually this isn't uploaded to github, but for the sake of the midterm demo, I have uploaded it
- info logs are recored whenever a change occurs within the program (app starting, commands registering, etc)
- warning logs are recorded whenever a non fatal mistake occurs, like the user trying to divide by zero
- error logs are recorded whenever a fatal problem occurs, such as a file not being found

### Design Patterns for Scalable Architecture

Incorporate key design patterns to address software design challenges, including:
- **Facade Pattern:** Offer a simplified interface for complex Pandas data manipulations.
- **Command Pattern:** Structure commands within the REPL for effective calculation and history management.
- **Factory Method, Singleton, and Strategy Patterns:** Further enhance the application's code structure, flexibility, and scalability.

## Development, Testing, and Documentation Requirements

### Testing and Code Quality

- Achieve a minimum of 90% test coverage with Pytest.
- Ensure code quality and adherence to PEP 8 standards, verified by Pylint.

### Version Control Best Practices

- Utilize logical commits that clearly group feature development and corresponding tests, evidencing clear development progression.

### Comprehensive Documentation

- Compile detailed documentation in `README.md`, covering setup instructions, usage examples, and an in-depth analysis of architectural decisions, particularly emphasizing the implementation and impact of chosen design patterns and the logging strategy.
