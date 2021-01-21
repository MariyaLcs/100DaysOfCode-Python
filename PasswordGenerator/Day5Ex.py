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

