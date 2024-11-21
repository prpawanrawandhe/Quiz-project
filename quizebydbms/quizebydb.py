import random
import mysql.connector

username = 'user1'
password = 'user1'

def login():
    print("\ntemperory usrname is user1 and pass is user1\n")
    a = input("Enter Username : ")
    b = input("Enter Password : ")

    if a == username and b == password:
        print(f"successfully login as {a} \n")
        return True

    else:
        print("\nWrong username and password")
        login()

def con(sub,sn):

    query = f"SELECT* FROM {sub} WHERE sn = {sn};"

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            auth_plugin='mysql_native_password',
            database='data'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            cursor.execute(query)

            connection.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

    tup = cursor.fetchone()
    return tup
    
def registration():
    a= input("/nif you doesn't want to register press 's' otherwise press : ")
    if a == 's':
        return

    name = input("please enter your name : ")
    email = input("please enter your email : ")
    user = input("please create username : ")
    passwd = input("please create password : ")
    print("Registration successful!")


def check():
    ans = input("Enter Ans :")
    if ans == 'A' or ans == 'a':
        ans = 2
        return ans
    elif ans == 'B' or ans == 'b':
        ans = 3
        return ans
    elif ans == 'C' or ans == 'c':
        ans = 4
        return ans
    elif ans == 'D' or ans == 'd':
        ans = 5
        return ans
    else:
        print("please give proper input and try again")
        return check()


def quize():
    sub = None
    right = 0
    wrong = 0
    a = input("\nEnter subject you want to attempt quize \n1.OPP's\n2.DBMS\n3.OS\nYour Ans: ")

    if a == '1' or a == "OPP's":
        sub = 'opps'
    elif a == '2' or a == "DBMS":
        sub = 'dsa'
    elif a == '3' or a == "OS":
        sub = 'os'  
    else:
        print("please give proper input and try again")
        return quize()
    
    for i in range(5):
        n = random.randint(1,10)

        tup = con(sub,n)
        print(f"\n{i+1}. {tup[1]}\n")
        print(f"A){tup[2]}")
        print(f"B){tup[3]}")
        print(f"C){tup[4]}")
        print(f"D){tup[5]}\n")

        ans = check()

        if tup[ans] == tup[6]:
            right += 1

        else:
            wrong += 1

        print("right =",right,", wrong =",wrong)
    return [right,wrong]


def score(r,w):
    print(f"\nNo. of right Ans : {r}")
    print(f"No. of wrong Ans : {w}")
    print(f"\nYour score : {(r/5)*100}\n")

def run():
    a = quize()
    score(a[0],a[1])

    b = input("press 'e' for exit or press enter to attempt more quiz : ")

    if b == 'e':
        print("thank you!!")
        return
    run()
    


def welcome():
    print("\n~ WELCOME TO QUIZE ROUNDS ~")
    registration()
    login()
    run()
    





welcome()
