"""
x = int(input("Enter a number: "))
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")
"""
def main():
    x = int(input("Enter a number: "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")
def is_even(n):
    """
    if n % 2 == 0:
        return True
    else:
        return False
        """
   #return True if n % 2 == 0 else False
    return n % 2 == 0
main()
   

