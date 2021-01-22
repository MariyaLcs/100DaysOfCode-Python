#Ex1 Average Height
#180 124 165 173 189 169 146
# no use len() or sum() after #######

student_heights = input("Input a list of student heights ").split()

sum=0
length=0

for n in range(0, len(student_heights)):
    ##############
    student_heights[n] = int(student_heights[n])
    length+=1
    sum+=student_heights[n]

average_height = round(sum/length)
print(average_height)

#Ex2 Highest Score
#78 65 89 86 55 91 64 89
# no use max() after #######

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
# print(student_scores)

##############

highest_score = student_scores[0]

for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"The highest score in the class is: {highest_score}")

#Ex3 Adding Evens

total = 0
for number in range(2, 101, 2):
  total +=number
  print(number)
print(total)

#Ex4 FizzBuzz

for number in range(1, 101):
  if number%5==0 and number%3==0:
    print("FizzBuzz")
  elif number%3==0:
    print("Fizz")
  elif number%5==0:
    print("Buzz")
  else:
    print(number)