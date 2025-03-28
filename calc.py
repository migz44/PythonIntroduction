# calc

# x = input("Enter X:")
# y = input("Enter Y:")

# convert a string to number
while True:
    try:
        num1 = float(input("Enter X: "))
        num2 = float(input("Enter Y: "))
        if num2 == 0:
            print("Cannot divide by zero. Try again.")
            continue
        result = num1 / num2
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")
