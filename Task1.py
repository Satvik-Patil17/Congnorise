
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

print("Select operation:")
print("A. Add")
print("S. Subtract")
print("M. Multiply")
print("D. Divide")

while True:
    choice = input("Enter choice (A/S/M/D): ")

    if choice in ('A', 'S', 'M', 'D'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 'A':
            print("Result:", add(num1, num2))
        elif choice == 'S':
            print("Result:", subtract(num1, num2))
        elif choice == 'M':
            print("Result:", multiply(num1, num2))
        elif choice == 'D':
            print("Result:", divide(num1, num2))
        break
    else:
        print("Invalid Input")
