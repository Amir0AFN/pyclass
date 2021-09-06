#Amir Abbas Fattahi - Thursday 14-18 class
# tamrin BMI nesbatan pishrafte ;)
def bmi_resault(weight ,height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_report(bmi):
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

def height_input():
    raw_height = int(input("Your height: "))
    if raw_height > 5:
        height = raw_height / 100
        return height
    else:
        height = raw_height
        return height

height = height_input()
weight = int(input("Your weight: "))

bmi = bmi_resault(weight ,height)
print("Your BMI: ",bmi)
bmi_report(bmi)
