import pytest
from Exercise_11_3 import Employee

@pytest.fixture
def employee(): 
    employee = Employee('Ashhad', 'Mazhar', 5000)
    return employee

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.salary == 10000

def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.salary == 15000