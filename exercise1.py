'''exercise : 1 calculator program in python'''

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2

elif operation == '-':
    result = num1 - num2

elif operation == '*':
    result = num2 * num1 

else :
    result = num1 / num2 

print("the result is : " , result)  