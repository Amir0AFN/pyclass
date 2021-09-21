#Amir Abbas Fattahi - Thursday 14-18 class
#tamrin miangin adad list
numbers = []
def get_list():
    while True:
        number = int(input("Enter your number:\n"))
        if number == 0:
            break
        numbers.append(number)

def calculate_average():
    length = len(numbers)
    majmoo = sum(numbers)
    average = majmoo / length
    print(f"majmoo = {majmoo}")
get_list()
calculate_average()
