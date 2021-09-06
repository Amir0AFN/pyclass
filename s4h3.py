#Amir Abbas Fattahi - Thursday 14-18 class
#tamrin etehad haye riyazi
print('''type1 =morabaE_do_jomleE
type2 =morabaE_se_jomleE
type3 =mokaabE_do_jomleE
type4 =mozdavaj
type5 =jomle_moshtarak
type6 =chagh_o_laughar''')
def type1(n1 ,n2 ,type):
    if type == "majmo":
        resault = n1**2 + n2**2 + 2*n1*n2
        print("(a + b)^2 =",resault)
    else:
        resault = n1**2 + n2**2 - 2*n1*n2
        print("(a - b)^2 =",resault)
def type2(n1 ,n2 ,n3):
    resault = n1**2+nr2**2+n3**2+2*n1*n2+2*n1*nr3+2*n2*n3
    print("(a + b + c)^2 =",resault)
def type3(n1 ,n2 ,type):
    pass
def type4(n1 ,n2):
    resault = (n1-n2)*(n1+n2)
    print("(a - b)(a + b) =",resault)
def type5(n1 ,n2 ,moshtarak):
    resault = moshtarak**2 + (n1+n2)*moshtarak + (n1*n2)
    print("(x + a)(x + b) =",resault)
def type6(n1 ,n2 ,type):
    if type == "majmo":
        resault =(n1+n2)*(n1**2-n1*n2+n2**2)
        print("a^3 + b^3 =",resault)
    else:
        resault = (n1-n2)*(n1**2+n1*n2+n2**2)
        print("a^3 - b^3 =",resault)

def type_of_mathematical_alliance(type):
    if type == "type1":
        n1 = int(input("Enter number1:\n"))
        n2 = int(input("Enter number2:\n"))
        type = input("Type:\n")
        type1(n1 ,n2 ,type)
    elif type == "type2":
        n1 = int(input("Enter number1:\n"))
        n2 = int(input("Enter number2:\n"))
        n3 = int(input("Enter number3:\n"))
        type2(n1 ,n2 ,n3)
    elif type == "type3":
        n1 = int(input("Enter number1:\n"))
        n2 = int(input("Enter number2:\n"))
        type = input("Type:\n")
        type3(n1 ,n2 ,type)
    elif type == "type4":
        n1 = int(input("Enter number1:\n"))
        n2 = int(input("Enter number2:\n"))
        type4(n1 ,n2)
    elif type == "type5":
        n1 = int(input("Enter number1:\n"))
        n2 = int(input("Enter number2:\n"))
        moshtarak = int(input("Enter moshtarak:\n"))
        type5(n1 ,n2 ,moshtarak)
    elif type == "type6":
        n1 = int(input("Enter number1:\n"))
        n2 = int(input("Enter number2:\n"))
        type = input("Type:\n")
        type6(n1 ,n2 ,type)

type = input("Enter type:\t")

type_of_mathematical_alliance(type)
