#boolean expression - has a true or false answer
x = int(input("Enter value for x:"))
y = int(input("Enter value for y:"))

#using only if 
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")

#using elif
if x > y :
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y") #this is optional for elif

# or keyword
if x>y or x < y:
    print("x is not equal to y")
else :
    print("x is equal to y")

if x!=y :
    print("x is not equal to y")
else:
    print("x is equal to y")

