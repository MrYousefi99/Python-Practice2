print("Please Insert Your Weight ")

W = float(input())

print("Please Insert Your Height in cm")

h = float(input())
H = h*0.01

Bmi = W/H**2
print("Your BMI is : ", Bmi)


if Bmi<18.5 :
   print("Your Weight is UnderWeight")

if Bmi>18.5 and Bmi<24.9 :
     print("Your Weight is Normal")

if Bmi>25 and Bmi <29.9 :
   print("Your Weight is OverWeight")

if Bmi>= 30 and Bmi<34.9 :
   print("Your Weight is Obese")

if Bmi>35 :
   print("Your Weight is Extremely")