while True:
    try:
        numerator = int(input("Enter numerator: "))
        denominator = int(input("Enter denominator: "))
        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        print(f"Divison is = {numerator /  denominator}")
        break
    except ValueError:
        print("input is not integer")
    except ZeroDivisionError as e:
        print(e)