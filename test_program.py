from tests import square
def main():
    test_square()

#assert keyword

def test_square():
    """
    if square(2)!= 4:
        print("2 square was not 4")
    if square(3)!=4:
        print("3 square was not 9")
    """
    try:
        assert square(3)==9
    except AssertionError:
        print("3 square was not 9")

if __name__ == "__main__":
    main()

#if we do this it creates a code that is very large
#so we use a third party tool called pytest
