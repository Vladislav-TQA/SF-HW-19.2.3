import pytest
import requests
from app.calculator import Calculator


class TestCalc: # тестируем весь калькулятор нажатием на стрелку
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self): # умножение
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculate_correctly(self): # деление
        assert self.calc.division(self, 9, 3) == 3

    def test_subtraction_calculate_correctly(self): # вычитание
        assert self.calc.subtraction(self, 5, 3) == 2

    def test_adding_calculate_correctly(self): # сложение
        assert self.calc.adding(self, 7, 2) == 9
