from app.calculations import add, subtract, multiply, divide

def test_add():
    print("testing add funtion")
    assert add(5,3) == 8

def test_subtract():
    assert subtract(9, 4) == 5


def test_multiply():
    assert multiply(4, 3) == 12


def test_divde():
    assert divide(20, 5) == 4

