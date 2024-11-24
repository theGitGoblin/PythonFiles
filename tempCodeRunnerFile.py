

#second attempt at oop



class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade



class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.student = []

    def add_students(self, student):
            if len(self.student) < self.max_students:
                self.student.append(student)
                return True
            return False   
    def get_AverageGrade(self, grade):
        pass



course = Course("CompSci 1101", 5)

s1 = Student("Jeremy", 21, 90)

course.add_students(s1)

s2 = Student("Alexys", 22, 100)

course.add_students(s2)

s3 = Student("Jeron", 24 , 35)

course.add_students(s3)

print(course.student[2].name)


