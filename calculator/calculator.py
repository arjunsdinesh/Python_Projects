def addition(a, b):
    result = a + b
    print("The sum = " + str(result))

def subtraction(a, b):
    result = a - b
    print("The difference = " + str(result))

def multiply(a, b):
    result = a * b
    print("The product = " + str(result))

def division(a, b):
    try:
        result = a / b
        print("The result = " + str(result))
    except ZeroDivisionError:
        print("Division by zero not possible\n")
        print("Enter a valid number")

def main():
    while True:
        print("Calculator:\nThe operations are -->\n")
        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. EXIT!!!\n")

        choice = int(input("Enter your choice: "))

        if choice == 5:
            break

        a = int(input("Enter 1st number: "))
        b = int(input("Enter 2nd number: "))

        if choice == 1:
            addition(a, b)
        elif choice == 2:
            subtraction(a, b)
        elif choice == 3:
            multiply(a, b)
        elif choice == 4:
            division(a, b)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

main()
