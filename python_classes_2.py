# person class
from datetime import date, datetime


class Person:
    def __init__(self, name, dob, gender, disabled):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.disabled = disabled

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Dob: {self.dob}")
        print(f"Gender: {self.gender}")
        if self.disabled:
            print("disabled")
        else:
            print("enabled")
        print("---------------------")

    def get_age(self):
        current_date = datetime.today()
        date_birth = datetime.strptime(self.dob, "%d-%m-%Y")
        age = current_date - date_birth
        print("Age is", age.days // 365)


p1 = Person("Hamilton", "5-02-1985", "Male", "False")
p2 = Person("Norris", "5-02-1985", "Female", "True")
p3 = Person("Piastri", "5-02-1985", "Male", "false")
p4 = Person("Verstappen", "5-02-1985", "Male", "False")
p5 = Person("Russel", "5-02-1985", "Female", "True")
p6 = Person("Leclerc", "5-02-1985", "Female", "True")
p7 = Person("Antonelli", "5-02-1985", "Male", "false")
p8 = Person("Tsunoda", "5-02-1985", "Male", "false")
p9 = Person("Hadjar", "5-02-1985", "Male", "false")
p10 = Person("Albon", "5-02-1985", "Male", "false")

p1.print_details()
p1.get_age()
