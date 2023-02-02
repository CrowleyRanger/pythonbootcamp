import pandas as pd

student_dict = {"student": ["Lemoren", "Garrafus", "Lancaster"], "score": [76, 54, 91]}

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(row.student)
