# Given the names and grades for each student in a class of  students 
# Store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

students = []

for _ in range(int(input('Enter # of Students: '))):
    
    name = input('Enter Student Name: ')
    score = float(input('Enter Student\'s Score: '))
    # students.append([name, score])
    students.append([score, name])

students.sort()
print(students)
del students[2:]

for x in students:
    for y in x:
        if isinstance(y, str):
            print(y)




