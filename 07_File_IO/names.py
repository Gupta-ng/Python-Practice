"""
name = input("what's your name? ")
print(f"hello, {name}")
"""
"""
names = []
for _ in range(3):
    names.append(input("whats's your name? "))
for name in sorted(names):
    print(f"hello, {name}")
"""
"""
name = input("what's your name? ")
file = open("names.txt", "w") # only writes one name in names.txt
file.write(f"{name}\n")
file.close()
"""
"""
name = input("what's your name? ")
file = open("names.txt", "a") # append all names and shows every name in names.txt
file.write(f"{name}\n")
file.close()
"""
"""
name = input("what's your name? ")
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
"""
"""
with open("names.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    print("hello,", line)
"""
"""
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
"""
"""
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print(f"hello, {name}")
"""
"""
with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())
"""
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names, reverse=True):
    print(f"hello, {name}")

