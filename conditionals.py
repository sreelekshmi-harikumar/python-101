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

def main():
    num = int(input("Enter a number:"))
    if is_even(num):
        print("It is an even number")
    else:
        print("It is an odd number")

# bool - can be True or False
def is_even(num):
    if num %2 == 0 :
        return True
    else:
        return False

main()

#Pythonic language
#return True if num % 2 == 0 else False
#return (num % 2 == 0)

#match - keyword - used for pattern matching
name = input("Enter your hogwarts house:")
match name:
    case "Gryffindor":
        print("Bravery and courage")
    case "Hufflepuff":
        print("Loyalty and patience")
    case "Ravenclaw":
        print("Intelligence and wit")
    case "Slytherin":
        print("Ambition and cunning")
    case _:
        print("Not a valid house")
        