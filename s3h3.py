#Amir_Abbas_Fattahi_14-18-Thursday
#amaliat ashkal hendesi
shape = input('''Choose a geometric shape:
(Circle ,Triangle ,Square ,Diamond ,Rectangle ,Rhombos ,Trapezoid)
''')
operation = input(''''Operation?
(Area ,Perimeter)
''')
pi = 3.14
if shape.lower() == "circle":
    radius = float(input("Radius: "))
    if operation == "area":
        print(pi * radius**2)
    else:
        print(2 * radius * pi)
elif shape.lower() == "triangle":
    height = int(input("Height: "))
    base = int(input("Base: "))
    if operation == "area":
        print((base * height)/2)
    else:
        print(base * 3)
elif shape.lower() == "square":
    length = int(input("Length: "))
    if operation == "area":
        print(length * length)
    else:
        print(4 * length)
elif shape.lower() == "diamond":
    if operation == "area":
        f_base = int(input("First base: "))
        s_base = int(input("Second base: "))
        print(f_base * s_base)
    else:
        length = int(input("Length: "))
        print(4 * length)
elif shape.lower() == "rectangle":
    length = int(input("Length: "))
    width = int(input("Width: "))
    if operation == "area":
        print(length * width)
    else:
        print((2 * length)+(2 * width))
elif shape.lower() == "rhombos":
    height = int(input("Height: "))
    base = int(input("Base: "))
    print(height * base)
elif shape.lower() == "trapezoid":
    f_base = int(input("First base: "))
    s_base = int(input("Second base: "))
    height = int(input("Height: "))
    print((f_base + s_base) * height/2)
