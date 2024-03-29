'''Testing OPerations'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide, log

def test_operation_add():
    '''Testing the addition operation'''
    calculation = Calculation(Decimal('10'), add, Decimal('5'))
    assert calculation.perform_two_operands() == Decimal('15'), "Add operation failed"

def test_operation_subtract():
    '''Testing the subtract operation'''
    calculation = Calculation(Decimal('10'), subtract,Decimal('5'))
    assert calculation.perform_two_operands() == Decimal('5'), "Subtract operation failed"

def test_operation_multiply():
    '''Testing the multiply operation'''
    calculation = Calculation(Decimal('10'), multiply,Decimal('5'))
    assert calculation.perform_two_operands() == Decimal('50'), "Multiply operation failed"

def test_operation_divide():
    '''Testing the divide operation'''
    calculation = Calculation(Decimal('10'), divide,Decimal('5'))
    assert calculation.perform_two_operands() == Decimal('2'), "Divide operation failed"

def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('10'), divide, Decimal('0'),)
        calculation.perform_two_operands()

def test_operation_log_one():
    '''Testing the log operation'''
    calculation = Calculation(Decimal('10'), log)
    assert calculation.perform_one_operand() == Decimal('1'), "Log operation failed"

def test_operation_log_two():
    '''Testing the log operation'''
    calculation = Calculation(Decimal('9'), log, Decimal('3'),)
    assert calculation.perform_two_operands() == Decimal('2'), "Log operation failed"

def test_invalid_logarithm_one():
    '''Testing the <= 0 logarithm exception'''
    with pytest.raises(ValueError, match="Logarithm undefined for zero or negative numbers"):
        calculation = Calculation(Decimal('-10'), log)
        calculation.perform_one_operand()

def test_invalid_logarithm_two():
    '''Testing the <= 0 logarithm exception'''
    with pytest.raises(ValueError, match="Logarithm undefined for base <= 1"):
        calculation = Calculation(Decimal('10'), log, Decimal('-4'),)
        calculation.perform_two_operands()
