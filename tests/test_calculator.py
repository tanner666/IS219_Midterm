"""Test for main calculator startup"""
import pytest
import os
import sys
from calculator import Calculator

@pytest.fixture
def calculator(monkeypatch):
    # Setup
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    calc = Calculator()
    calc.start()
    yield calc
    # Teardown
    # (Any required cleanup steps)

def test_logging_configured(capfd,monkeypatch):
    Calculator()
    captured = capfd.readouterr()
    assert "Logging configured." in captured.err

def test_environment_variables_loaded(capfd, monkeypatch):
    Calculator()
    captured = capfd.readouterr()
    assert "Environment variables loaded." in captured.err

def test_register_commands_logging(capfd, monkeypatch):
    # Assuming you have a test command to load
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    calc = Calculator()
    calc.start()
    captured = capfd.readouterr()
    print(captured)
    assert "Command 'add' from plugin 'add' registered." in captured.err

def test_app_get_environment_variable():
    calculator = Calculator()
#   Retrieve the current environment setting
    current_env = calculator.get_environment_variable('ENVIRONMENT')
    # Assert that the current environment is what you expect
    assert current_env in ['DEVELOPMENT', 'TESTING', 'PRODUCTION'], f"Invalid ENVIRONMENT: {current_env}"

def test_calculator_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    calculator = Calculator()
    calculator.start()
    captured = capfd.readouterr()
    assert "Type 'exit' to exit." in captured.err  # Verify the initial print statement

def test_interrupted_by_keyboard(capfd, monkeypatch):
    # Mock 'input' to immediately trigger an exit
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    calc = Calculator()
    calc.start()
    pytest.raises(SystemExit)
    captured = capfd.readouterr()
    assert "Application shutdown." in captured.err