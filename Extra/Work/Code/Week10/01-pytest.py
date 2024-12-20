import pytest

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class TestCalculator:

    # This setup method runs before each test method
    def setup_method(self):
        self.calc = Calculator()  # Create an instance of Calculator for each test

    def test_add(self):
        result = self.calc.add(3, 5)
        assert result == 8  # Check if 3 + 5 equals 8

    def test_subtract(self):
        result = self.calc.subtract(10, 4)
        assert result == 6  # Check if 10 - 4 equals 6

    def test_multiply(self):
        result = self.calc.multiply(4, 5)
        assert result == 20  # Check if 4 * 5 equals 20

    def test_divide(self):
        result = self.calc.divide(10, 2)
        assert result == 5  # Check if 10 / 2 equals 5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            self.calc.divide(10, 0)  # Check if ValueError is raised when dividing by 0
