#int - integer 
#it is also a function in python and not just a data type
x = int(input("Enter an integer:")) #this is called type conversion
y = int(input("Enter another integer:"))

#Addition 
add = x + y 
#Subtraction 
sub = x - y
#Multiplication
mul = x * y 
#Division 
div = x/y
#Modulus
mod = x%y
print("Addtion is",add)
print("Subtraction is",sub)
print("Multiplcation is",mul)
print(f"Division is {div:.2f}")
print("Modulus is",mod)

#float - a number with decimal point

m = float(input("Enter a float number:"))
n = float(input("Enter another float number:"))

#to round floating point numbers
mul_float = m * n 
l = round(mul_float,2) #round(number[,ndigits]) -rounds a number to a given precision in decimal digits (default 0 digits).
print(l)

