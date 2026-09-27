#syntax error is completely on us to correct
#run time errors occurs when the program runs

x = int(input("Enter a number:"))
print(f"x is {x}")

#ValueError is when you type the wrong literal
#literals are values that we type

try:
    y = int(input("Enter a value:"))
    print(f"y is {y}")
except ValueError:
    print("The input should be an integer")

#NameError - when we use a local scope variable somewhere else
try :
    z = int(input("Enter:"))
except ValueError:
    print("Incorrect format entered")
else:
    print(f"The value is {z}")

#makes sure else is only executed if try is successful

while True:
    try:
        number = int(input("Enter a number:"))
    except ValueError:
        print("Enter again")
        continue
    else:
        break
print(f'The number is {number}') #runs only after getting value hence no NameError

#if this was a functio then just return x instead of breaking

def main():
    n = get_int("What's n?")
    print(f"The value is:{n}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            #print("Invalid value,try again")
            #or just do
            pass 

main()
#we can also raise exceptions using raise
