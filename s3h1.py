#Amir_Abbas_Fattahi-Thursday-14-18-class
#BMI
h = float(input("Your height(m)? \n"))
m = float(input("Your mass(Kg)? \n"))
bmi = int(m/(h**2))
print("Your BMI: " + str(bmi))

if bmi < 16:
    print("You are severe thin.")
elif bmi < 17:
    print("You are moderate thin.")
elif bmi < 18.5:
    print("You are mild thin.")
elif bmi < 25:
    print("You are normal.")
elif bmi < 30:
    print("You are overweight.")
elif bmi < 35:
    print("You are obese class 1")
elif bmi < 40:
    print("You are obese class 2")
elif bmia > 40:
    print("You are obese class 3")
