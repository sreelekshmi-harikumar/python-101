def main():
    c = input("Enter the string value:")
    hello(c)

def hello(to="world"):
    return f"hello {to}"

if __name__ == "__main__":
    main()
