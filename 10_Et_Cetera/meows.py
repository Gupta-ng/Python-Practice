"""
for i in range(3):
    print("meow")
"""

"""
MEOWS = 3

for i in range(MEOWS):
    print("meow")
"""

class Cat:
    MEOWS = 3
    
    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")
cat = Cat()
cat.meow()


