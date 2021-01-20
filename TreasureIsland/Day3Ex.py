#Ex1

number = int(input("Which number do you want to check? "))

###################################

if number % 2 == 0:
  print("This is an even number")
else:
  print("This is an odd number")

#Ex2

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

###################################

BMI = round(weight/height**2, 1)
if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are underweight")
elif BMI < 25:
  print(f"Your BMI is {BMI}, you have a normal weight")
elif BMI < 30:
  print(f"Your BMI is {BMI}, you are slightly overweight")
elif BMI < 35:
  print(f"Your BMI is {BMI}, you are obese")
else:
  print(f"Your BMI is {BMI}, you are clinically obese")