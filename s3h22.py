#Amir Abbas Fattahi - Thursday 14-18 class
#Math operation
def math_operation(number1 ,number2 ,operation):
    if operation == "plus":
        print(number1 + number2)
    elif operation == "minus":
        print(number1 - number2)
    elif operation == "times":
        print(number1 * number2)
    elif operation == "divide":
        print(number1 / number2)
    elif operation == "exponent":
        print(number1 ** number2)

math_operation(8 ,3 ,"divide")
