from hello import hello

def main():
    test_hello()

def test_hello():
    assert hello("David") == "hello David"
    assert hello() == "hello world"


if __name__ == "__main___":
    main()
