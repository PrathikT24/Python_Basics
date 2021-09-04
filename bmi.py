print("BMI Calculator")
height=float(input("Enter your height: \n "))
weight=int(input("Enter your weight: \n "))
bmi=round(weight/(height)**2)
if bmi<18.5:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi<25:
    print(f"Your bmi is {bmi}, you are normal weight")
elif bmi<30:
    print(f"Your bmi is {bmi}, you are overweight")
elif bmi<35:
    print(f"Your bmi is {bmi}, you are obese")
else:
    print(f"Your bmi is {bmi}, you are clinically obese")




