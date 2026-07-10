while True:
    try:
        x = int(input("what's the x? "))
        y = int(input("what's the y? "))
        print(f"sum = {x + y}")
        break
    except ValueError:
        print("input is not number")
