def main():
    print_pattern(5)
def print_pattern(rows):
    for i in range(rows, 0, -1):
        print("*" * i)
main()