from tests import square 
import pytest

def main():
    test_square()
    test_positive()
    test_negative()
    test_zero()
    test_str()

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")


if __name__ == "__main__":
    main()

'''
    Because python is on your Windows PATH, 
    but the folder containing the pytest executable isn't on your PATH.
'''
