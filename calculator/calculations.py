from decimal import Decimal
from typing import Callable, List

from calculator.calculation import Calculation

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        '''new calc to history'''
        cls.history.append(calculation)
    
    @classmethod
    def get_history(cls) -> List[Calculation]:
        '''get history of calcs'''
        return cls.history
    
    @classmethod
    def clear_history(cls):
        '''clear history'''
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        '''get latest clac, return none if none exists'''
        if cls.history:
            return cls.history[-1]
        return None
    
    @classmethod
    def find_by_operation(cls,operation_name:str) ->List[Calculation]:
        '''find and return list of calcs by operation'''
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]