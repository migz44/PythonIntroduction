# BMI calc
weight = 68
height = 1.75
bmi = weight/(height*height)

if bmi < 18.5:
    print("Under weight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Normal")
elif 25 <= bmi <= 29.9:
    print("Overweight")
elif bmi >= 30 and bmi <= 34.9:
    print("Obese")
elif bmi >= 35 and bmi <= 39.9:
    print("Severely obese")
else:
    print(" Morbidly Obese")