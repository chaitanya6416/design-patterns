class Student:
    def __init__(self, roll, name, phone):
        self.roll = roll
        self.name = name
        self.phone = phone

class StudentBuilder:
    roll = None
    name = None
    phone = None
    def setRoll(self, roll):
        self.roll = roll
        return StudentBuilder
    def setName(self, name):
        self.name = name
    def setPhone(self, phone):
        self.phone = phone

