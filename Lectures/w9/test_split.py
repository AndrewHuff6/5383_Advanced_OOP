# to run, just say "pytest" in the terminal
import pytest   
from exceptions import split_ticket

def test_zero_people1():
    with pytest.raises(ValueError):
        split_ticket(100,0)

#def test_zero_people2():
#    with pytest.raises(ValueError):
#        split_ticket(100,20)
        
def test_zero_people3():
    with pytest.raises(ValueError):
        split_ticket(0,0)

def test_value_5():
    assert split_ticket(100,20) == 5

#split_ticket(-100,20)
#val = split_ticket(100,20)
#print(val)
