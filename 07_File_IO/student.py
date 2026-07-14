"""
with open("07_File_IO/students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
"""
"""
with open("07_File_IO/students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
"""
"""
students = []
with open("07_File_IO/students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")
for student in sorted(students):
    print(student)
"""
"""
students = []
with open("07_File_IO/students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student ={}
        student["name"] = name
        student["house"] = house
        students.append(student)
    for student in students:
        print(f"{student['name']} is in {student['house']}")
"""
"""
students = []
with open("07_File_IO/students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student ={"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}") 
"""
"""
students = []
with open("07_File_IO/students.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",")
        student ={"name": name, "home": home}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
"""
"""
import csv

students = []

with open("07_File_IO/students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
"""
"""
import csv

students = []

with open("07_File_IO/students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
"""
"""
import csv

name = input("what's your name? ")
home = input("where's your home? ")

with open("07_File_IO/students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
"""

import csv

name = input("what's your name? ")
home = input("where's your home? ")

with open("07_File_IO/students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
