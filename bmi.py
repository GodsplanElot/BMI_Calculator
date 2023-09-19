#algorithm for bmi
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
print (bmi)

if bmi< 18.5:
    print("your underweight")
elif 18.5 <= bmi <24.9:
    print ("normal weight")
elif 25 <= bmi < 29.9:
    print ("Overweight")
else:
    print ("Obese")
    
        
print(f"Your BMI is: {bmi:.2f}")
