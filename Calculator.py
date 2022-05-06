#addition function
def add (x, y):
    return x + y

#subtraction function
def subtract (x, y):
    return x - y

#multiplication function
def multiply (x , y):
    return x * y

#division function
def divide (x , y):
    return x / y

#asks the user to enter 2 numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#asks the user to select an operation
operation = int(input("Please choose an operation: \n"
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n"))

#if the user wants to add
if operation == 1:
    print(num1 , " + " , num2 ," = " , add(num1, num2))

#user wants to subtract
elif operation == 2:
    print(num1 , " - " , num2," = " , subtract(num1, num2))

#user wants to multiply
elif operation == 3:
    print(num1 , " * " , num2, " = " , multiply(num1, num2))

#user wnats to divide
elif operation == 4:
    print(num1 , " / " , num2, " = " , divide(num1, num2))

#if the user enters an invalid operation
else:
    print("Invalid input!")

