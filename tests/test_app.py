from myapp.app import app

def test_add():
    assert app.add(2, 3) == 5
    assert app.add(-1, 1) == 0
    assert app.add(0, 0) == 0
    assert app.add(-1, -1) == -2

def test_subtract():
    assert app.substract(5, 3) == 2
    assert app.substract(-1, 1) == -2
    assert app.substract(0, 0) == 0
    assert app.substract(-1, -1) == 0

def test_multiply():
    assert app.multiply(2, 3) == 6
    assert app.multiply(-1, 1) == -1
    assert app.multiply(0, 5) == 0
    assert app.multiply(-1, -1) == 1

def test_divide():
    assert app.divide(6, 3) == 2
    assert app.divide(-1, 1) == -1
    assert app.divide(0, 1) == 0
    assert app.divide(-1, -1) == 1

