#Amir Abbas Fattahi - Thursday 14-18 class
#tamrin mohasebat hendesi
pi = 3
def circle():
    operation = input("operation: ")
    radius = int(input("radius: "))
    if operation == "area":
        print(radius ** 2 * pi)
    else:
        print(2 * radius * pi)
def triangle():
    operation = input("operation: ")
    height = int(input("height: "))
    base = int(input("base: "))
    if operation == "area":
        print(base * height / 2)
    else:
        print(3 * base)
def square():
    operation = input("operation: ")
    length = int(input("length: "))
    if operation == "area":
        print(length ** 2)
    else:
        print(4 * length)
def diamond():
    operation = input("operation: ")
    length = int(input("length: "))
    firs_base = int(input("firs_base: "))
    second_base = int(input("second_base: "))
    if operation == "area":
        print(firs_base * second_base / 2)
    else:
        print(4 * length)
def rectangle():
    operation = input("operation: ")
    length = int(input("length: "))
    width = int(input("width: "))
    if operation == "area":
        print(length * width)
    else:
        print((length + width) * 2)
def cube():
    operation = input("operation: ")
    length = int(input("length: "))
    width = int(input("width: "))
    height =int(input("height: "))
    if operation == "volume":
        print(length * width * height)
    elif operation == "surface area":
        print(((length*width)*2)+((length*height)*2)+(width*height)*2)
def cylinder():
    operation = input("operation: ")
    radius = int(input("radius: "))
    height = int(input("height: "))
    if operation == "volume":
        print((radius ** 2 * pi)*height)
    elif operation == "surface area":
        print(((2 * pi * radius)*height) + 2 * (radius ** 2 * pi))
def sphere():
    operation = input("operation: ")
    radius = int(input("radius: "))
    if operation == "volume":
        print(4/3 * pi * radius ** 3)
    elif operation == "surface area":
        print(4 * pi * radius ** 2)

def geometric_shape(shape):

    if shape == "circle":
        circle()
    elif shape == "triangle":
        triangle()
    elif shape == "square":
        square()
    elif shape == "diamond":
        diamond()
    elif shape == "rectangle":
        rectangle()
    elif shape == "cube":
        cube()
    elif shape == "cylinder":
        cylinder()
    elif shape == "sphere":
        sphere()

shape = input("shape: ")
geometric_shape(shape)
