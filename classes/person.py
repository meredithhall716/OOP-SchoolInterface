class Person: 
    def __init__(self, name, age, role, school_id, password):
        self.name = name
        self.age = age
        self.role = role
        self.school_id = school_id
        self.password = password

    def __str__(self) :
        return f'Name: {self.name}\tRole: {self.role}\tID: {self.school_id}'

