name = input("what is your name? ")
"""
if name == "Harry":
    print("Gryffindor")
elif name == "Hrmione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
else:
    print("Who are you?")
"""
"""
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who are you?")
"""
"""
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who are you?")
"""

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who are you?")