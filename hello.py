print("hello") 

def calculator():
    print("=== Welcome to the Simple Calculator ===")
    
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    print("Choose an Operation: + - * /")
    operator = input("Enter the operation: ")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operator! Please choose from +, -, *, /")
        return

    print(f"Result: {num1} {operator} {num2} = {result}")

calculator()










