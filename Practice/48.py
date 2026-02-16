# *args

def analyze_numbers(*args):
    sum = args[0]
    max = args[0]
    min = args[0]
    count = 1 if args[0] % 2 == 0 else 0
    for num in args[1:]:
        sum += num
        if num > max:
            max = num
        if num < min:
            min = num
        if num % 2 == 0:
            count += 1
    return sum, max, min, count

print(analyze_numbers(4, 7, 2, 9, 10))



# **kwargs

def student_result(**kwargs):
    total = 0
    cnt = 0
    for mark in kwargs.values():
        total += mark
        cnt += 1
    avg = total / cnt
    grade = None
    if avg >= 90:
        grade = 'A'
    elif avg >= 75:
        grade = 'B'
    elif avg >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return total, avg, grade

print(student_result(math=90, physics=80, chemistry=85))