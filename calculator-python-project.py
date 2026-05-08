print("--- Welcome to Python Simple Calculator ---")

while True:

    print("\nAvailable Operations:")
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")

    option = input("\nChoose operation: ")

    if not option.isdigit():
        print("Warning: Please enter a number (1-4).")
        continue

    option = int(option)

    if option not in [1, 2, 3, 4]:
        print("Warning: Invalid choice. Select 1-4 only.")
        continue

    num1 = input("\nEnter first number: ")
    num2 = input("Enter second number: ")

    if not num1.replace(".", "").isdigit() or not num2.replace(".", "").isdigit():
        print("Warning: Please enter valid numbers only.")
        continue

    num1 = float(num1)
    num2 = float(num2)

    if option == 1:
        result = num1 + num2

    elif option == 2:
        result = num1 - num2

    elif option == 3:
        result = num1 * num2

    elif option == 4:
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            continue
        result = num1 / num2

    print(f"> Result: {result:.2f}")

    again = input("\nDo another calculation? (y/n): ")

    if again.lower() != "y":
        print("Calculator stopped.")
        break
