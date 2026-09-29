import csv #the csv library

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file) #csv.reader(file)
    """
    The reader looks like this:
    {"name": "Hermoine", "home": "Pivot House"}
    {"name": "Ron", "home": "The Burrow"}
    {"name": "Harry", "home": "Number four,Pivet high"}
    {"name": "Draco", "home": "Malffoy House"}

    """
    for row in reader: #we dont use split since we need to do a code where it doesnt split on comma inside the quotes
          students.append({"name":row["name"],"home":row["home"]})
    """
    for line in file:
        name,home = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["home"] = home
        students.append(student)#creates a list of dictionaries
    """
'''
def get_house(student):
    return student["house"]
'''
#lambda is a function that has no name

for student in sorted(students,key=lambda student:student["name"]): #where student is the parameter
        print(student)

## writing in csv

name = input("What is your name?")
home = input("Where is your home?")

with open("students.csv","a") as f:
      writer = csv.DictWriter(f,fieldnames=["name","home"])#csv.writer(f)
      writer.writerow({"name":name,"home":home})