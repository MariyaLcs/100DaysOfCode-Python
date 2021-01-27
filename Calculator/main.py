#Part1
#https://repl.it/@MashaPodosinova/calculator-start#main.py
from art import logo
print(logo)

# add
def add(n1, n2):
    return n1 + n2

# subtract
def subtract(n1, n2):
    return n1 - n2

# multiply
def multiply(n1, n2):
    return n1 * n2

# divide
def divide(n1, n2):
    return n1 / n2

operations = {"+" : add, "-" : subtract, "*" : multiply, "/" : divide}

num1 = int(input("What is the first number? "))
num2 = int(input("What is the next number? "))

for operation in operations:
    print(operation)

operation_symbol = input("Pick an operation from the line above ")
# result = eval(num1 + operation + next_number)
result = operations[operation_symbol](num1, num2)

print(f"{num1}  {operation_symbol}  {num2} = {result}")