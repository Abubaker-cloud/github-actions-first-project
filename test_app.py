from app import greet, add, multiply

def test_greet():
    assert greet("Abubaker") == "Hello, Abubaker!"

def test_add():
  assert add(10, 20) == 30

def test_add_negative():
    assert add(-5, 5) == 0

def test_multiply():
    assert multiply(5, 3) == 15