"""
print("#")
print("#")
print("#")
"""

#for _ in range(3):
   # print("#")

'''
def main():
    print_column(3)

def print_column(n):
    print("#\n"*n,end='')

main()

'''
"""
def main():
    print_row(4)

def print_row(n):
    print("#"*n)

main()
"""
#nested loop
def main():
    print_square(4)

def print_square(n):
    for i in range(n):
        for j in range(n):
            print("#",end='')
        print() #after each row we need a new line

main()

#orrr
def main_two():
    print_column(4)

def print_column(n):
    for _ in range(n):
        print_row(n)

def print_row(n):
    print("$"*n)

main_two()
    