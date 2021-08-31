#Amir_Abbas_Fattahi-Thursday-14-18-class
#Math Operation
number1 = float(input("First number: "))
number2  = float(input("Second number: "))
operation = input("Which math operation?\n")

if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    print(number1 / number2)
elif operation == "**":
    print(number1 ** number2)
elif operation == "** 1/n":
    print(number1 ** (1/number2))
