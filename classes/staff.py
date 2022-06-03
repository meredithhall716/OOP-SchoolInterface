import csv
from classes.person import Person

class Staff(Person):
    def all_staff():
        staff = []
        with open('data/staff.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            first_row = next(spamreader)
            for row in spamreader:
                # print(f'Compiling staff...{row}')
                staff.append(Staff(*row))
        return staff