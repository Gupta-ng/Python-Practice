"""
for i in range(3):
    print("#")
"""
"""
def main():
    print_coulumn(3)

def print_coulumn(heights):
    for _ in range(heights):
        print("#")
       # print("#\n" * heights, end="")
main()
"""

"""
def main():
    print_row(4)
def print_row(width):
    print("?" * width)
main()
"""
def main():
    print_square(4)
def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
    
main()
        