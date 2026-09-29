students = []

with open("students.csv","r") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)#creates a list of dictionaries
'''
def get_house(student):
    return student["house"]
'''
#lambda is a function that has no name

for student in sorted(students,key=lambda student:student["name"]): #where student is the parameter
        print(student)

