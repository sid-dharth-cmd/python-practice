marks = {
    'A': 40,
    'B': 44, 
    'C': 35, 
    'D': 48, 
    'E': 28
    }
max = 0
student = 'O'
for key in marks:
    if marks[key] > max:
        max = marks[key]
        student = key
print(f"Student with highest marks is {student} with marks {max}")