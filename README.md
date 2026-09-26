Python 101 🐍

A self-guide for me and others who come across it.

Data Types

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

print("Hello", "World", sep=" ", end="\n")


sep — separates multiple values. Default: " "

end — specifies what is printed at the end. Default: "\n"

Check the official Python documentation for more details.

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
