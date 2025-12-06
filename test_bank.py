from bank import value


def test_hello():
     assert value("hello") == 0
     assert value("hello guys") == 0
     assert value("hello, guys") == 0


def test_h():
    assert value("h") == 20


def test_else():
    assert value("wow") == 100

def test_Hello():
    assert value("Hello") == 0
    assert value("Hello world") == 0


def test_H():
    assert value("H") == 20

