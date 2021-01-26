#Ex1 Grading Program
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades={}

for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key]="Outstanding"
    elif student_scores[key] >= 81:
        student_grades[key]="Exceeds Expectations"
    elif student_scores[key] >= 71:
        student_grades[key]="Acceptable"
    else:
        student_grades[key]="Fail"

print(student_grades)

#Ex2 Dictionary in List
def add_new_country(name, number, cities):
    new={}
    new["country"]=name
    new["visits"]=5
    new["cities"]=cities
    
    travel_log.append(new)

    print(f"You've visited {name} {number} times")
    print(f"You've been to {cities[0]} and {cities[1]}")


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)




