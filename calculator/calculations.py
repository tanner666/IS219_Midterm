"""Calculations history class"""
import pandas as pd
import logging
from decimal import Decimal
from typing import Callable, List

from calculator.calculation import Calculation

class Calculations:

    #self is for instances, cls is for classes
    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the calculator history file"""
        current_calc = pd.DataFrame({'Operation': [calculation.operation.__name__], 'A': [calculation.a], 'B':[calculation.b]})
         # Append the DataFrame to the CSV file
        # If the file doesn't exist, it creates one and writes the header
        # If the file exists, it appends without writing the header
        with open('./calculator/history.csv', 'a',newline='') as f:
            current_calc.to_csv(f, header=f.tell()==0, index=False)

    @classmethod
    def get_history(cls) -> List[List[str]]:
        """Retrieve the entire history of calculations"""
        try:
            history = pd.read_csv('./calculator/history.csv')
            return history.values.tolist()
        except FileNotFoundError:
            logging.error("No history found.")
    
    @classmethod
    def clear_history(cls):
        """Clear the calculator's history"""
        empty_df = pd.DataFrame(columns=['Operation', 'A', 'B'])
        # Overwrite the existing file with the empty DataFrame
        empty_df.to_csv('./calculator/history.csv', index=False)
        logging.info("History cleared.")

    @classmethod
    def get_latest(cls) -> List[str]:
        """Get the most recently added calculation or return None"""
        try:
            history = pd.read_csv('./calculator/history.csv')
            return history.values.tolist()[0]
        except FileNotFoundError:
            logging.error("No history found.")

    @classmethod
    def remove_latest(cls):
        """Remove the most recently added calculation or return None"""
        try:
            history = pd.read_csv('./calculator/history.csv')
            history = history.iloc[:-1, :]
            with open('./calculator/history.csv', 'w', newline='') as f:
                history.to_csv(f, header=f.tell()==0, index=False)
        except FileNotFoundError:
            logging.error("No history found.")
        except Exception as e:
            logging.error("Exception: {e}")
    
    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[List[str]]:
        """Find and return a list of calculations by operation name"""
        try:
            history = pd.read_csv('./calculator/history.csv').values.tolist()
            print(history)
            return [calc for calc in history if calc[0] == operation_name]
        except FileNotFoundError:
            logging.error("No history found.")  
