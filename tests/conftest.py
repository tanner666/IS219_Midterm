"""Faker tests with fixtures"""
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide, log

fake = Faker()

# pylint: disable=line-too-long
# pylint: disable=trailing-whitespace
# pylint: disable=comparison-with-callable

def generate_test_data(num_records):
    """Define operation mappings for both Calculator and Calculation tests"""
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide,
        'log': log
    }
    # Generate test data
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        # use first Decimal() if _ % 4 != 3, else use second Decimal()
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        # Randomly obtain operation_name from map
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]
        
        # Ensure a/b is not zero for divide and log operations to prevent division by zero in expected calculation
        if operation_func == divide: # pragma: no cover
            b = Decimal('1') if b == Decimal('0') else b
        if operation_func == log: # pragma: no cover
            a = Decimal('1') if a <= Decimal('0') else a
            b = Decimal('10') if b <= Decimal('1') else b

        try: # pragma: no cover
            if operation_func == divide and b == Decimal('0'):
                expected = "Cannot divide by zero"
            else:
                expected = operation_func(a, b)
        except ValueError: # pragma: no cover
            expected = "Cannot divide by zero"

        try: # pragma: no cover
            if operation_func == log and a <= Decimal('0'):
                expected = "Logarithm undefined for zero or negative numbers"
            elif operation_func == log and b <= Decimal('1'):
                expected = "Logarithm undefined for base <= 1"
            else:
                expected = operation_func(a, b)
        except ValueError: # pragma: no cover
            expected = "Logarithm undefined for zero or negative numbers"
        
        yield a, operation_name, operation_func, b, expected

def pytest_addoption(parser):
    """Add new command line options for pytest"""
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """Check if the test is expecting any of the dynamically generated fixtures"""
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        # Adjust the parameterization to include both operation_name and operation for broad compatibility
        # Ensure 'operation_name' is used for identifying the operation in Calculator class tests
        # 'operation' (function reference) is used for Calculation class tests.
        parameters = list(generate_test_data(num_records))
        # Modify parameters to fit test functions' expectations
        modified_parameters = [(a, op_name if 'operation_name' in metafunc.fixturenames else op_func, b, expected) for a, op_name, op_func, b, expected in parameters]
        metafunc.parametrize("a,operation,b,expected", modified_parameters)
