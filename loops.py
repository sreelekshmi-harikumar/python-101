#while can be used to repeated do an action that the while condition statisfies
i = 3
while (i!=0):
    print("meow")
    i = i - 1#if i is not decreased then it will be an infinite loop

#another way 
i = 1 
while( i <=3):
    print("meow")
    i = i + 1 #also can be written as i+=1 
#python doesn't have i++ or i-- operators like C or C++ so we have to use i+=1 or i-=1

#for loop is used when we know how many times we want to repeat an action 
#The difference between while and for loop is that while loop is used when we do not know how many times we have to repeat an action and for loop is used when we know how many times we have to repeat an action
#This is because for loop is used over a condition  
#for loop is used to iterate over a sequence (like a list, tuple or string) 
for i in [1,2,3]:
    print("meow")

for _ in range(3): #function that returns a range of numbers
    print("meow") #_ is  used when we dont need that value

for i in range(10):
    print(i)

print("meow"*3)
print("meow\n"*3,end="")

#validating input
while True:
    n = int(input("Enter a value:"))
    if n<0:
        continue #continue to stay within this loop
    else:
        break

# another way is
while True:
    num = int(input("Enter a positive value:"))
    if n>0:
        print("Valid value inputted")
        break

for _ in range(n):
    print("hellooooo")

def main():
    meow(3)

def meow(n):
    n = get_num(n)
    for _ in range(n):
        print("meow")

def get_num(n):
    while True:
        n = int(input("Enter an integer:"))
        if n>0:
            break
    return n 
main()
