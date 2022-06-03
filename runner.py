from classes.school import School 
from classes.student import Student

school = School('Ridgemont High') 

print(school.name)
# print(school.staff)
# print(school.students)

print('STAFF')
for item in school.staff:
    print(item)

print('STUDENTS')
for item in school.students:
    print(item)

# student_info = {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}
# student1 = Student(**student_info)

# student_info = ['Meredith',17, 'Student',12345,'password']
# student2 = Student(*student_info)

# student3 = Student('Zack',17, 'Student',12345,'password')

# print(student1.name)
# print(student2.name)
# print(student3.name)