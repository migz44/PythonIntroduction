# car [make, model, dare_of_make,drive_side]
# get age
# allowed in kenya
# print_details
from datetime import datetime


class Car:
    def __init__(self, make, model, date_of_make, drive_side):
        self.make = make
        self.model = model
        self.date_of_make = date_of_make  # Ensure date_of_make is a string in "DD-MM-YYYY" format
        self.drive_side = drive_side  # Assign drive_side

    def get_age(self):
        current_date = datetime.today()
        date_of_make = datetime.strptime(self.date_of_make, "%d-%m-%Y")
        age = (current_date - date_of_make).days // 365  # Convert days to years
        return age

    def car_permitted(self):
        age = self.get_age()
        return "Not permitted in KENYA" if age >= 7 else "Permitted in KENYA"

    def car_permitted_2(self):
        return "Left Drive Side Not Permitted in Kenya" if self.drive_side.lower() == "left" else "Right Drive Side Permitted in Kenya"

    def details(self):
        print(f'Make: {self.make}')
        print(f'Model: {self.model}')
        print(f'Date of Make: {self.date_of_make}')
        print(f'Drive Side: {self.drive_side}')
        print(f'Car Age: {self.get_age()} years')
        print(f'Car Status: {self.car_permitted()}')
        print(f'Drive Side Status: {self.car_permitted_2()}')
        print("--------------------------------")


# Corrected instantiation with proper date format
car_1 = Car("Ford", "Mustang", "01-01-2008", "left")
car_2 = Car("Toyota", "Corolla", "15-06-2015", "right")
car_3 = Car("Honda", "Civic", "10-03-2012", "right")
car_4 = Car("BMW", "X5", "20-08-2010", "left")
car_5 = Car("Mercedes", "C-Class", "05-12-2017", "right")
car_6 = Car("Nissan", "Altima", "25-07-2013", "left")
car_7 = Car("Mazda", "CX-5", "30-09-2018", "right")
car_8 = Car("Subaru", "Forester", "12-02-2016", "right")
car_9 = Car("Volkswagen", "Golf", "28-04-2011", "left")
car_10 = Car("Chevrolet", "Camaro", "17-11-2014", "left")
car_11 = Car("Hyundai", "Tucson", "08-05-2019", "right")

car_1.details()
car_2.details()
car_3.details()
car_4.details()
car_5.details()
car_6.details()
car_7.details()
car_8.details()
car_9.details()
car_10.details()