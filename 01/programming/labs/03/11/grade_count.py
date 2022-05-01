a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if (a > 100 or a < 0) or (b > 100 or b < 0) or (c > 100 or c < 0)\
or (d > 100 or d < 0) or (e > 100 or e < 0):
    print("None")
    exit()
elif (a == 0) and (b == 0) and (c == 0) and (d == 0) and (e == 0):
    print("Average grade = 0 -> F")
else:
    percent_grade = float((a+b+c+d+e)/5)
    if 100 >= percent_grade >= 90:
        letter_grade = 'A'
    elif 90 > percent_grade >= 82:
        letter_grade = 'B'
    elif 82 > percent_grade >= 75:
        letter_grade = 'C'
    elif 75 > percent_grade >= 67:
        letter_grade = 'D'
    elif 67 > percent_grade >= 60:
        letter_grade = 'E'
    elif 60 > percent_grade >= 0:
        letter_grade = 'F'
    print("Average grade =", percent_grade, "->", letter_grade)