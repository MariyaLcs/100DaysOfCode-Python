#Ex1 Odd/Even

number = int(input("Which number do you want to check? "))

###################################

if number % 2 == 0:
  print("This is an even number")
else:
  print("This is an odd number")

#Ex2 BMI(v2)

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

#Ex3 Leap Year

year = int(input("Which year do you want to check? "))

###################################

if year%4==0:
  if  year%100==0:
    if  year%400==0:
      print("Leap year")
    else:
      print("Not a Leap year")
  else:
    print("Leap year")
else:
  print("Not a Leap year")

#Ex4 Pizza Order

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

###################################

price=0
if size=="S":
  price+=15
  if add_pepperoni=="Y":
    price+=2
elif size=="M":
  price+=20
  if add_pepperoni=="Y":
    price+=3
elif size=="L":
  price+=25
  if add_pepperoni=="Y":
    price+=3
if extra_cheese=="Y":
  price+=1

print(f"Your final bill is: £{price}")

#Ex5 Love Calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

###################################

names_combined = name1.lower()+name2.lower()

t_count = names_combined.count("t")
r_count = names_combined.count("r")
u_count = names_combined.count("u")
e_count = names_combined.count("e")

l_count = names_combined.count("l")
o_count = names_combined.count("o")
v_count = names_combined.count("v")

true_sum = t_count+r_count+u_count+e_count
love_sum =l_count+o_count+v_count+e_count

total = str(first_sum)+str(second_sum)
love_score=int(total)

if love_score<10 or love_score>90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score>40 and love_score<50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")