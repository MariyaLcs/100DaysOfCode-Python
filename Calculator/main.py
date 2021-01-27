from art import logo
print(logo)

first_number = (input("What is the first number? "))
operation = input("+   -   *   /   \nPick an operation ")
next_number = (input("What is the next number? "))

calculation = True

def math(first_number, operation, next_number):
    result = eval(first_number + operation + next_number)
    print(f"{first_number}  {operation}  {next_number} = {result}")
    return result
math(first_number, operation, next_number)