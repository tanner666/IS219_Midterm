# pylint: disable=redefined-outer-name, unused-argument
"""Testing calculator history methods"""

import os
import pytest
import pandas as pd
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add
from calculator.operations import multiply

# Fixture to manage the setup and teardown of a test environment
@pytest.fixture
def setup_and_teardown_file():  # pylint: disable=inconsistent-return-statements
    """Fixture for setting up/tearingdown file"""
    # Setup: copy the history file before each test
    try:
        initial_history = pd.read_csv('./calculator/history.csv')
        Calculations.clear_history()
    except FileNotFoundError:
        return "File not found error"
    yield
    # Replace history with original
    with open('./calculator/history.csv', 'w', newline='') as f:  # pylint: disable=unspecified-encoding
        initial_history.to_csv(f, header=f.tell()==0, index=False)

def test_add_calculation(setup_and_teardown_file):
    """Testing adding to history"""
    calculation = Calculation(1, add, 2)
    Calculations.add_calculation(calculation)
    history = pd.read_csv('./calculator/history.csv')
    assert len(history) == 1
    assert history.iloc[0].to_dict() == {'Operation': 'add', 'A': 1, 'B': 2}

def test_get_history(setup_and_teardown_file):
    """Testing retrieving the entire history"""
    calculation = Calculation(1, add, 2)
    Calculations.add_calculation(calculation)
    history = Calculations.get_history()
    assert history == [['add', 1, 2]]

def test_clear_history(setup_and_teardown_file):
    """Testing clearing file history"""
    calculation = Calculation(1, add, 2)
    Calculations.add_calculation(calculation)
    Calculations.clear_history()
    assert not os.path.exists('./calculator/history.csv') or pd.read_csv('./calculator/history.csv').empty # pylint: disable=line-too-long

def test_get_latest(setup_and_teardown_file):
    """Testing retrieving latest calculation"""
    calculation1 = Calculation(1, add, 2)
    calculation2 = Calculation(3, add, 4)
    Calculations.add_calculation(calculation1)
    Calculations.add_calculation(calculation2)
    latest = Calculations.get_latest()
    assert latest == ['add', 1, 2]

def test_remove_latest(setup_and_teardown_file):
    """Testing removing latest calculation"""
    calculation1 = Calculation(1, add, 2)
    calculation2 = Calculation(3, add, 4)
    Calculations.add_calculation(calculation1)
    Calculations.add_calculation(calculation2)
    Calculations.remove_latest()
    history = Calculations.get_history()
    assert history == [['add', 1, 2]]

def test_find_by_operation(setup_and_teardown_file):
    """Testing finding by operation name"""
    calculation_add = Calculation(1, add, 2)
    calculation_add2 = Calculation(8, add, 2)
    calculation_multiply = Calculation(3, multiply, 4)
    Calculations.add_calculation(calculation_add)
    Calculations.add_calculation(calculation_add2)
    Calculations.add_calculation(calculation_multiply)
    found = Calculations.find_by_operation('add')
    print(found)
    assert len(found) == 2
