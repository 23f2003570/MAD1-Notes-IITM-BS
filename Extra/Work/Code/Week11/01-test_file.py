import pytest

def func(x, y):
    out = x**2 + y**2
    return out

class Test_class0():
    def test_case1(self):
        assert func(1,2) == 5
        
    def case_test2(self):
        assert func(2,3) == 13
        
    def case_test3(self):
        assert func(6,2) == 38
        
class Test_class1():
    def test_case1(self):
        assert func(5,2) == 29
    def case_test2(self):
        assert func(1,1) == 12
        
    