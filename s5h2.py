#Amir Abbas Fattahi - Thursday 14-18 class
#tamrine tarkib list ha
list1 = []
number1 = int(input("Enter a number:\t"))
list1.append(number1)
number2 = int(input("Enter a number:\t"))
list1.append(number2)
number3 = int(input("Enter a number:\t"))
list1.append(number3)
list2 = []
number4 = int(input("Enter a number:\t"))
list2.append(number4)
number5 = int(input("Enter a number:\t"))
list2.append(number5)
number6 = int(input("Enter a number:\t"))
list2.append(number6)
list3 = []
number7 = int(input("Enter a number:\t"))
list3.append(number7)
number8 = int(input("Enter a number:\t"))
list3.append(number8)
number9 = int(input("Enter a number:\t"))
list3.append(number9)
list1.extend(list2 + list3)
list1.sort(reverse = True)
print(list1)
print(list1[::2])
