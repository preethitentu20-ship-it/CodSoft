                 # Simple Calculator
# Taking input from user
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
# Choosing operatio
print("Choose operation what you want to perform:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
choice = input("Enter choice (+, -, *, /): ")
# Performing calculation
if choice == '+':
    result = n1 + n2
    print("Result =", result)
elif choice == '-':
    result = n1 - n2
    print("Result =", result)
elif choice == '*':
    result = n1 * n2
    print("Result =", result)
elif choice == '/':
    if n2 != 0:
        result = n1 / n2
        print("Result =", result)
    else:
        print("Division by zero is not allowed")
else:
    print("Invalid operation choice")