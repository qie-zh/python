class Student:
    def __init__(self,number,name,grade1,grade2,grade3) -> None:
        self.name = name
        self.number = number
        self.grade = []
        self.grade.append(int(grade1))
        self.grade.append(int(grade2))
        self.grade.append(int(grade3))

li = []
for _ in range(int(input())):
    number,name,grade1,grade2,grade3 = input().split()
    student = Student(number,name,grade1,grade2,grade3)
    li.append(student)
max_grade = 0

for i in li:
    if sum(i.grade) > max_grade:
        max_i = i
        max_grade = sum(i.grade)

print('%s %s %d'%(max_i.name,max_i.number,sum(max_i.grade)))