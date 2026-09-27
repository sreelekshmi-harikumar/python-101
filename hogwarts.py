students = ["Hermoine","Ron","Harry"] #list of strings

# A key pointing to a single string value
my_dict = {"name": "Alice"}

# A key pointing to a list of values
my_dict = {"fruits": ["apple", "banana", "cherry"]}

print(students[0]) #prints Hermoine
print(students[1]) #prints Ron 
print(students[2]) #prints Harry

for name in students:
    print(name)

for name in range(len(students)):
    print(name+1,students[name])

#dictionaries - allows to associate one value with another
houses = {
    "Hermonie":"Gryffinder",
    "Cederic":"Hufflepuff",
    "Luna":"Ravenclaw",
    "Draco":"Slytherin"
}

print(houses["Cederic"])
for student in houses:
    print(student) #by default it just iterates over the keys

for student in houses:
    print(student,houses[student],sep=":")

#list of dictionaries
students = [
    {"name":"Hermoine","house":"Gryffindor","patronous":"Otter"},
    {"name":"Haryy","house":"Gryffindor","patronous":"Stag"},
    {"name":"Draco","house":"Slytherin","patronous":None}
]
#None keyword refers to absence of a value

for student in students:
    print(student)

for student in students:
    print("Name:"+student["name"],student["house"],student["patronous"],sep=",")


