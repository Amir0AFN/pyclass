#Amir Abbas Fattahi - Thursday 14-18 class
#Geometric operation
pi = 3.14
def geometric_operation(shape ,operation ,length ,width ,radius ,base ,height):
    if shape == "circle":
        if operation == "area":
            print(radius ** 2 * pi)
        else:
            print(2 * radius * pi)
    elif shape == "triangle":
        if operation == "area":
            print(base * height /2)
        else:
            print(3 * base)
    elif shape == "square":
        if operation == "area":
            print(lenth ** 2)
        else:
            print(4 * length)
    elif shape == "rectangle":
        if operation == "area":
            print(length * width)
        else:
            print((2 * length) + (2 * width))
    elif shape == "rhombos":
        print(base * height)

geometric_operation("circle" ,"area" ,0 ,0 ,4 ,0 ,0)
