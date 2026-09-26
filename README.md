# Python 101 
(A self-guide for me and others who come across it)

# Data Types

Data types represent the different kinds of values that variables can store in Python.

Data Type	Python Type	Example
Integer	int	42
String	str	"Hello"
Floating-point number	float	3.14
Built-in Functions
print()

Used to display output.

print("Hello, World!")


Useful parameters:
print()
print(*objects, sep=' ', end='\n', file=None, flush=False)


Documentation definition:

Prints the values of objects to the text stream file, separated by sep and followed by end. sep, end, file, and flush, if present, must be given as keyword arguments.

Parameters:

objects — The values to be printed.

sep — String inserted between values. Default: ' '.

end — String appended after the last value. Default: '\n'.

file — An object with a write(string) method. Default: sys.stdout.

flush — Whether to forcibly flush the stream. Default: False.

int()

Converts a value to an integer when possible.

x = int("42")

input()

Takes input from the user and returns it as a string.

name = input("Enter your name: ")

String Functions / Methods

Assuming var is a string:

var.split()

Splits a string into a list.

text = "Hello World"
print(text.split())
# ['Hello', 'World']

var.upper()

Converts the string to uppercase.

"hello".upper()
# "HELLO"

var.lower()

Converts the string to lowercase.

"HELLO".lower()
# "hello"

var.capitalize()

Capitalizes the first character of the string.

"hello world".capitalize()
# "Hello world"

var.strip()

Removes leading and trailing whitespace.

"  hello  ".strip()
# "hello"

var.title()

Capitalizes the first letter of each word.

"hello world".title()
# "Hello World"

Defining a Function

Functions are defined using the def keyword.

def greet():
    print("Hello!")


To call the function:

greet()

Function with Parameters
def greet(name):
    print("Hello,", name)

greet("Alice")

Notes

This README is a work in progress. I'll keep adding Python concepts as I learn them.
