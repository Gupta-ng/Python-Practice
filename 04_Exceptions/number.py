"""
x = int(input("what's x? "))
print(f"x is {x}") # if type any string, it will give ValueError
"""
"""
try:
    x = int(input("what's x? "))
   # print(f"x is {x}")
except ValueError:
    print("x is not a integer")
#print(f"x is {x}") # it will give NameError
else:
    print(f"x is {x}")
"""

"""
while True:
    try:
        x = (int(input("what's the x? ")))
    except ValueError:
        print("x is not a integer")
    else:
        break
print(f"x is {x}")
"""

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("what's the x? "))
           # x = int(input("what's the x? "))
        except ValueError:
           pass
            
           """ print("x is not a integer")
        else:
            return x """

main()
     