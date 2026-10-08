while True:
     try:
         weight=float(input("Please add your weight as kilogram"))
         height=float(input("Please add your height as a metr"))
     except ValueError:
         print("Please add an integer and dont use any symbol or letter.")
     else:
         break
Bmi=weight/(height**2)
if Bmi<18.5:
     print("Underweight")
elif Bmi>=18.5 and Bmi<=24.9:
     print("Normal weight")
elif Bmi>=25.0 and Bmi<=29.9:
     print("Overweight")
else:
     print("Obese")