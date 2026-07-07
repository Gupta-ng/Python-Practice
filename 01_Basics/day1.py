"""
this is a multi-line comment

name = input("what is your name? ")
print("Hello, " + name + "!") 
print("Hello,", end =" ")
print(name)
print("Hello, \"Nayana\"")
print(f"Hello, {name}")
"""

"""
# That's a comment
name = input("what is your name? ").strip().title
name = name.strip() # Remove whitespace from the beginning and end of the string
name = name.capitalize() # Capitalize the first letter of the string
name = name.title() # Capitalize the first letter of each word in the string
name = name.strip().title() # Remove whitespace and capitalize the first letter of each word in the string
print(f"Hello, {name}")

"""
"""
def hello(to = "World"):
    print("Hello ,", to)
hello()
name = input("what is your name? ")
hello(name)

"""

def main():
    name = input("what is your name? ")
    hello(name)
def hello(to = "World"):
    print("Hello ," , to)
main()