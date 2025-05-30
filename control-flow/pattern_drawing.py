while True:
    try:
        size_str = input("Enter the size of the pattern: ")
        size = int(size_str)
        if size > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()
    row += 1