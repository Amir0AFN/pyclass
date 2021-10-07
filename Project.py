#Amir Abbas Fattahi - Thursday 14-18 class
#Contact project
print('''Enter:
(add) to create a new contact
(search) to find a contact
(remove) to delete a contact''')
import sqlite3
conn = sqlite3.connect('contact db.db')

def addition(info1, info2, number):
    import sqlite3
    conn = sqlite3.connect('contact db.db')
    cursor = conn.cursor()
    insert='insert into info values ("{}", "{}", {})'.format(info1, info2, number)
    cursor.execute(insert)
    conn.commit()
    conn.close()

def show_item(info1, info2):
    cursor = conn.cursor()
    select = '''select number from info where
     information1 = "{}" and information2 = "{}";'''.format(info1, info2)
    cursor.execute(select)
    result = cursor.fetchall()
    conn.commit()
    for row in result:
        print(row)
def remove_item(info1, info2):
    import sqlite3
    conn = sqlite3.connect('contact db.db')
    cursor = conn.cursor()
    remove_query = '''delete from info
    where information1 = "{}" and information2 = "{}"'''.format(info1, info2)
    cursor.execute(remove_query)
    conn.commit()
    conn.close()
while True:
    enterance = input("Enter the operator:\n")
    while enterance != "out":
        enterance.lower()

        if enterance == "add":
            cursor = conn.cursor()
            select_query1 = 'select information1 from info'
            cursor.execute(select_query1)
            result1 = cursor.fetchall()
            for items in result1:
                for item in items:
                    information1 = item
            select_query2 = 'select information2 from info'
            cursor.execute(select_query2)
            result2 = cursor.fetchall()
            for items2 in result2:
                for item2 in items2:
                    information2 = item2
            info1 = input("Name:\t")
            info2 = input("Last name:\t")
            number = int(input("Phone number:\t"))
            if info2 in information2 and info1 in information1:
                print("Contact exists.")
            else:
                addition(info1, info2, number)
                print("Phone number is added.")
            back = input("Do you want to go back? (Yes) or (No)\n")
            back.lower()
            if back == "yes":
                break

        elif enterance == "search":
            cursor = conn.cursor()
            select_query1 = 'select information1 from info'
            cursor.execute(select_query1)
            result1 = cursor.fetchall()
            for items in result1:
                for item in items:
                    information1 = item
            select_query2 = 'select information2 from info'
            cursor.execute(select_query2)
            result2 = cursor.fetchall()
            for items2 in result2:
                for item2 in items2:
                    information2 = item2
            print("please enter the informations:\n")
            info1 = input('Name:\t')
            info2 = input('Last name:\t')
            if info1 not in information1 or info2 not in information2:
                print("Contact does not exist!")
            elif info1 in information1 and info2 in information2:
                show_item(info1, info2)
            back = input("Do you want to go back? (Yes) or (No)\n")
            back.lower()
            if back == "yes":
                break
        elif enterance == "remove":
            import sqlite3
            conn = sqlite3.connect('contact db.db')
            cursor = conn.cursor()
            show_query = 'select * from info;'
            cursor.execute(show_query)
            result = cursor.fetchall()
            for item in result:
                print(item)
            print("please enter the informations:\n")
            cursor = conn.cursor()
            select_query1 = 'select information1 from info'
            cursor.execute(select_query1)
            result1 = cursor.fetchall()
            for items in result1:
                for item in items:
                    information1 = item
            select_query2 = 'select information2 from info'
            cursor.execute(select_query2)
            result2 = cursor.fetchall()
            for items2 in result2:
                for item2 in items2:
                    information2 = item2
            info1 = input('Name:\t')
            info2 = input('Last name:\t')
            if info1 not in information1 and info2 not in information2:
                print("Contact does not exist!")
            elif info1 in information1 and info2 in information2:
                remove_item(info1, info2)
                print("Contact removed.")
            back = input("Do you want to go back? (Yes) or (No)\n")
            back.lower()
            if back == "yes":
                break
