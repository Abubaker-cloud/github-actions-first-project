from app import greet, add

def test_greet():
    assert greet("Abubaker") == "Hello, Abubaker!"

def test_add():
  assert add(10, 20) == 50

def test_add_negative():
    assert add(-5, 5) == 0
