#BMI = (weight in pounds x pound)/ (height in inches x height in inches)

weight = float(input("Enter your weight in pound:"))
height = float(input("Enter your weight in inches:"))

BMI = (weight * 703 ) / ( height * height)

# print(weight)
# print(height)
# print(BMI)

if BMI < 18.5:
    print('Underweight')
elif BMI < 24.9:
    print('Healthy Weight')
elif BMI < 29.9:
    print("Overweight")
else:
    print('Obese')