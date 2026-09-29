#files are a way to storing information persistently
#name = input("Enter your name:")

from collections.abc import Sequence


class line(Sequence):
    """Represent one CSV line as a read-only sequence of fields."""

    def __init__(self, value, delimiter=","):
        self._fields = tuple(value.rstrip("\r\n").split(delimiter))

    def __getitem__(self, index):
        return self._fields[index]

    def __len__(self):
        return len(self._fields)

    def __repr__(self):
        return f"line({self._fields!r})"

    def __str__(self):
        return ",".join(self._fields)

"""
#file = open("names.txt","w") #file name and mode, gives a pointer to file
file = open("names.txt","a")
file.write(f"{name}\n") #used to write the variable to file
# will close and save the file

#if we do this again , then the name will be overwrriten rather than being appending them 

file.close()
"""
'''
with open("names.txt","a") as file:
    file.write(f"{name}\n")
'''

with open("names.txt","r") as file:
    lines = file.readlines()

#for line in lines:
    #print(line,end = '')

#or

names = []

with open("names.txt") as file:
    for line in file: #also use sorted(file)
        names.append(line.rstrip())

for name in sorted(names,reverse="True"):#used to sort list
    print(name)

with open("students.csv") as f:
    '''
    for line in f:
        for value in line:
            print(value,sep=':',end='')
    '''

    for csv_line in f:
        row = line(csv_line)#row is a sequence of fields
        print(row[0]+" is in "+row[1])

