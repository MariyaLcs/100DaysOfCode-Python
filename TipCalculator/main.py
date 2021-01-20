#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
print("Welcome to the tip calculator")
total = input("What was the total bill? £")
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_of_people = input("How many people to split the bill? ")

#################################

total = float(total)
total_with_tips = total * (1+int(percentage)/100)
per_person = total_with_tips / int(num_of_people)
rounded = round(per_person,2)
# rounded = "{:.2f}".format(per_person) => .00

print(f"Each person should pay: £{rounded}")