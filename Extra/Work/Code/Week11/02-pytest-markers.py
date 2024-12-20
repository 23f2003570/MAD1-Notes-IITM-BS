import pytest

def square(x):
    sum = 0
    for counter in range(x):
        sum += x
        return sum
    
    
@pytest.mark.marker1
def testcase_1():
    assert square(10) == 100 # square(10) = 10
    
@pytest.mark.marker2
def testcase_2():
    assert square(4) == 4
    
@pytest.mark.marker3
def testcase_3():
    assert square(5) == 25

@pytest.mark.marker4
def testcase_4():
    assert square(6) == 6