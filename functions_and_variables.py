print("Hello World")
"""
pthon is also an interpretor 
functions - action or verb that lets to perform a specific task
eg: print function is a built-in function 
bugs - mistakes are that you make in your program 
"""
print("Whats your name")
input("Enter your name:")

#return variables 
name = input("Whats your name?") #this is used to ask user for their name
print("I see your name is",name) 

#also can be written as
print("I see you name is "+name)

#comments are notes to yourself
"""
str - string
what you can pass to a function is called parameters
when you give values to those parameters , it is then called arguments
"""
#to avoid printing to next line
print("hello, ",end="")
print(name)

#overriding seperator
print("hello,",name,sep="???")

#corner case - print a quote
print('hello,"friend"') #change outer quotes to single quotes
print("hello,\"friend\"")

#new way of printing
print(f"hello,{name}")

"""
suppose our variable is : name
1.to remove empty spaces - name.strip() note:to removes empty spaces at start and end
2.to convert to upper case - name.upper()
3.to convert to lower case - name.lower()
4.to convert to title case - name.title()
5.to convert the first letter to upper case - name.capitalize()

It can also be used to together
name = name.strip().upper()
"""
#to split the name 
full_name = "Sreelekshmi Harikumar"
first,last = full_name.split(" ")
print(first)
print(last)

#function is created using def keyword which means define
def hello(name):
    print(f"hello,{name}")

keke = input("Enter your name:")
hello(keke)

def Hello(to="world"):
    print(f"Hello {to}")

Hello()#Hello world

#definig main
def main():
    age = int(input("Enter your age:"))
    print(check_age(age))

def check_age(age):
    if age>=18:
        return("You are not a minor")
    else:
        return("You are a minor")

main()
