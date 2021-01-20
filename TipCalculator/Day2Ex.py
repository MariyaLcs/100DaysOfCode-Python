#Ex1

two_digit_number = input("Type a two digit number: ")

####################################

first =two_digit_number[0]
second =two_digit_number[1]
print(int(first)+int(second))

#Ex2

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

####################################

BMI = int(weight)/float(height)**2
print(int(BMI))

#Ex3

age = input("What is your current age? ")

####################################

years_left=90-int(age)
convert_to_month=years_left*12
convert_to_weeks=years_left*52
convert_to_days=years_left*365

print(f"You have {convert_to_days} days, {convert_to_weeks} weeks and {convert_to_month} month left")