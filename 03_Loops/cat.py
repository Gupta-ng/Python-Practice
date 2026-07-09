# While loop that prints "meow" three times
"""
i = 3
while i != 0:
    print("meow")
    i = i - 1
"""
"""
i = 1
while i<= 3:
    print("meow")
    i = i + 1
"""
"""
i = 0
while i < 3:
    print("meow")
    i += 1
"""

# for loop that prints "meow" three times
"""
for i in [0, 1, 2]: # list of numbers from 0 to 2
    print("meow")
"""
"""
for i in range(3): # range of numbers from 0 to 2
    print("meow")
"""
"""
for _ in range(3): # range of numbers from 0 to 2
    print("meow")
"""
# print("meow\n" * 3) # prints "meow" three times

#print("meow\n" * 3, end="") # prints "meow" three times without extra newline at the end
"""
while True:
    n = int((input("whats the n value? ")))
    if n > 0:
        break
for _ in range(n):
    print("meow")
"""
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("whats the n value? "))
        if n > 0:
            return n
def meow(n):
    for _ in range(n):
        print("meow")

main()