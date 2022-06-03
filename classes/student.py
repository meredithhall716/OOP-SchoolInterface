import csv
from classes.person import Person

class Student(Person):
    def all_students():
        students = []
        with open('data/students.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            first_row = next(spamreader)
            for row in spamreader:
                # print(f'Compiling student...{row}')
                students.append(Student(*row))
        
        return students