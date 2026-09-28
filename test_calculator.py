from tests import square 

def main():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4

if __name__ == "__main__":
    main()

'''
    Because python is on your Windows PATH, 
    but the folder containing the pytest executable isn't on your PATH.
'''