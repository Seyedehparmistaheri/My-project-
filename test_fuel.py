from fuel import convert, gauge
import pytest


def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/1") == 100

def test_convert_negative():
    with pytest.raises(ValueError):
        convert("-1/5")
    with pytest.raises(ValueError):
        convert("1/-5")
    with pytest.raises(ValueError):
        convert("-3/-5")



def test_convert_errors():
    with pytest.raises(ValueError):
        convert("x/y")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("5/4")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
