# list of students in Hogwarts
# students = ["Harry", "Hermione", "Ron"]
"""
print(students[0])
print(students[1])
print(students[2])
"""
"""
for student in students:
    print(student)
"""
"""
for i in range(len(students)):
    print(students[i])
"""
"""
for i in range(len(students)):
    print(i + 1, students[i]) # print the index + 1 and the student name
"""

# dictionary of students and their houses
"""
students = {
    "Harry": "Gryffindor",
    "Hermione": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}
"""
"""
print(students["Harry"]) # prints Gryffindor
print(students["Draco"]) # prints Slytherin
"""
"""
for student in students:
    print(student, students[student], sep = ", ") # prints the student name and their house
"""
students = [
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}  
]
for student in students:
    print(student["name"], student["house"], student["patronus"], sep = ", ") # prints the student name, house and patronus