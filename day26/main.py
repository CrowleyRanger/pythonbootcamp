import random

# numbers = [1, 2, 3]
# new_numbers = [(num + 1) for num in numbers]
# print(new_numbers)

# DOUBLED LIST
# doubled_numbers = [num*2 for num in range(1, 5)]
# print(doubled_numbers)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# longer_names = [name.upper() for name in names if len(name) >= 5]

students_scores = {student:random.randint(1, 100) for student in names}

passed_students = {student:students_scores[student] for student in students_scores if students_scores[student] > 60}
print("Students:", students_scores)
print("Those who passed:", passed_students)