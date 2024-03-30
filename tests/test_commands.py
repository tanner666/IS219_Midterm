'''Test Calculator Class'''
from unittest.mock import patch
from decimal import Decimal
import pytest
from calculator.commands.add import AddCommand
from calculator.commands.subtract import SubtractCommand
from calculator.commands.divide import DivideCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.log import LogCommand
from calculator.commands.clear_history import ClearHistoryCommand
from calculator.commands.history import HistoryCommand
from calculator.commands.menu import MenuCommand
from calculator.commands.undo import UndoCommand

# pylint: disable=line-too-long,redefined-outer-name,unused-argument
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract

# pytest.fixture is a decorator that marks a function as a fixture,
# a setup mechanism used by pytest to initialize a test environment.
# Here, it's used to define a fixture that prepares the test environment for calculations tests.
@pytest.fixture
def setup_calculations():
    """Clear history and add sample calculations for tests."""
    # Clear any existing calculation history to ensure a clean state for each test.
    Calculations.clear_history()
    # Add sample calculations to the history to set up a known state for testing.
    # These calculations represent typical use cases and allow tests to verify that
    # the history functionality is working as expected.
    Calculations.add_calculation(Calculation(Decimal('10'), add,  Decimal('5')))
    Calculations.add_calculation(Calculation(Decimal('20'), subtract, Decimal('3')))

def test_clear_history_command(setup_calculations):
    """Test clearing the entire calculation history."""
    # Clear the calculation history.
    command = ClearHistoryCommand()
    command.execute(input)
    # Assert that the history is empty by checking its length.
    assert len(Calculations.get_history()) == 0, "History was not cleared"

@patch('builtins.print')
@patch('builtins.input', side_effect=['2', '8'])
def test_undo_command(setup_calculations,mock_print):
    """Test undoing a command"""
    # Clear the calculation history.
    command1 = AddCommand()
    command2 = UndoCommand()
    command1.execute(input)
    size = len(Calculations.get_history())
    command2.execute(input)
    # Assert that the history is one less by checking its length.
    assert len(Calculations.get_history()) == size, "Last command wasn't deleted"

def test_history_command(setup_calculations):
    """Test  entire calculation history."""
    command = HistoryCommand()
    command.execute(input)
    # Assert that the history is empty by checking its length.
    assert len(Calculations.get_history()) == 2, "History does not contain the expected number of calculations"

@pytest.fixture
def menu_command():
    """Fixture"""
    return MenuCommand()

def test_menu_command(capsys, menu_command):
    """Testing menu command"""
    mocked_files = ['add.py', 'subtract.py', 'menu', '__init__.py', '__pycache__']

    with patch('os.listdir', return_value=mocked_files):
        menu_command.execute(None)

    captured = capsys.readouterr()
    # Expected output, given the mocked directory contents
    expected_output_lines = ['add.py\n', 'subtract.py\n']

    # Split the captured output into lines and filter out empty lines
    actual_output_lines = [line + '\n' for line in captured.out.split('\n') if line]

    assert actual_output_lines == expected_output_lines, "The command did not print the expected list of command files."

@patch('builtins.print')
@patch('builtins.input', side_effect=['2', '8'])
def test_add_command(mock_input, mock_print):
    '''Test that addition function works'''
    command = AddCommand()
    inputs=['3.5', '4.5']
    command.execute(inputs)
    # Verify that the result of 3.5 + 4.5 is printed correctly
    mock_print.assert_called_once_with("The result of 3.5 + 4.5 is equal to 8.0")

@patch('builtins.print')
@patch('builtins.input', side_effect=['2', '8'])
def test_add_command_fail(mock_input, mock_print):
    '''Test that addition function works'''
    command = AddCommand()
    inputs=['4.5']
    command.execute(inputs)
    # Verify that the result of 3.5 + 4.5 is printed correctly
    mock_print.assert_called_once_with("Invalid input. Please enter numbers in the format 'add a b'.")

@patch('builtins.print')
@patch('builtins.input', side_effect=['2', '8'])
def test_subtract_command(mock_input, mock_print):
    '''Test that addition function works'''
    command = SubtractCommand()
    inputs=['4.5', '3.5']
    command.execute(inputs)
    # Verify that the result of 3.5 + 4.5 is printed correctly
    mock_print.assert_called_once_with("The result of 4.5 - 3.5 is equal to 1.0")

@patch('builtins.print')
@patch('builtins.input', side_effect=['2', '8'])
def test_subtract_command_fail(mock_input, mock_print):
    '''Test that sub function fails'''
    command = SubtractCommand()
    inputs=['4.5']
    command.execute(inputs)
    # Verify that the result of 3.5 + 4.5 is printed correctly
    mock_print.assert_called_once_with("Invalid input. Please enter numbers in the format 'subtract a b'.")

@patch('builtins.print')
@patch('builtins.input', side_effect=['2', '8'])
def test_multiply_command(mock_input, mock_print):
    '''Test that addition function works'''
    command = MultiplyCommand()
    inputs=['3', '4']
    command.execute(inputs)
    # Verify that the result of 3.5 + 4.5 is printed correctly
    mock_print.assert_called_once_with("The result of 3 * 4 is equal to 12")

@patch('builtins.print')
@patch('builtins.input', side_effect=['2', '8'])
def test_multiply_command_fail(mock_input, mock_print):
    '''Test that multiply function fails successfully'''
    command = MultiplyCommand()
    inputs=['4.5']
    command.execute(inputs)
    # Verify that the result of 3.5 + 4.5 is printed correctly
    mock_print.assert_called_once_with("Invalid input. Please enter numbers in the format 'multiply a b'.")

@patch('builtins.print')
@patch('builtins.input', side_effect=['2', '8'])
def test_divide_command(mock_input, mock_print):
    '''Test that addition function works'''
    command = DivideCommand()
    inputs=['8', '2']
    command.execute(inputs)
    # Verify that the result of 3.5 + 4.5 is printed correctly
    mock_print.assert_called_once_with("The result of 8 / 2 is equal to 4")

@patch('builtins.print')
@patch('builtins.input', side_effect=['2', '8'])
def test_divide_command_fail(mock_input, mock_print):
    '''Test that division function works'''
    command = DivideCommand()
    inputs=['4.5']
    command.execute(inputs)
    # Verify that the result of 3.5 + 4.5 is printed correctly
    mock_print.assert_called_once_with("Invalid input. Please enter numbers in the format 'divide a b'.")

@patch('builtins.print')
@patch('builtins.input', side_effect=['2', '8'])
def test_log_command(mock_input, mock_print):
    '''Test that addition function works'''
    command = LogCommand()
    inputs=['2', '8']
    command.execute(inputs)
    # Verify that the result of 3.5 + 4.5 is printed correctly
    mock_print.assert_called_once_with("The result of log 2 (8) is equal to 3")

@patch('builtins.print')
@patch('builtins.input', side_effect=['2', '8'])
def test_log_command_fail(mock_input, mock_print):
    '''Test that addition function works'''
    command = LogCommand()
    inputs=['4.5']
    command.execute(inputs)
    # Verify that the result of 3.5 + 4.5 is printed correctly
    mock_print.assert_called_once_with("Invalid input. Please enter numbers in the format 'log base a'.")
