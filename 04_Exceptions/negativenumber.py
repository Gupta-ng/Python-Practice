while True:
    try:
        x = int(input("What's x? "))

        if x < 0:
            raise ValueError("Negative numbers are not allowed")

        print(f"x is {x}")
        break

    except ValueError as e:
        print(e)