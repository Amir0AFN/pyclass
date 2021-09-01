#Amir_Abbas_Fattahi-Thursday-14-18-class
#BMI (new)
def bmi(height ,mass):
    bmi = mass/height**2
    output = print("BMI:", mass/height**2)

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
        print("You are obese class 1.")
    elif bmi <= 40:
        print("You are obese class 2.")
    elif bmi > 40:
        print("You are obese class 3.")

bmi(1.8 ,110)
