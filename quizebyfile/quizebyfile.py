import random
import json

with open('data.json','r') as j_file:
    data = json.load(j_file)


OS = data['os']

DSA = data['dsa']

OPPS  = data['opps']




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

def check():
    ans = input("Enter Ans :")
    if ans == 'A' or ans == 'a':
        ans = 0
        return ans
    elif ans == 'B' or ans == 'b':
        ans = 1
        return ans
    elif ans == 'C' or ans == 'c':
        ans = 2
        return ans
    elif ans == 'D' or ans == 'd':
        ans = 3
        return ans
    else:
        print("please give proper input and try again")
        return check()


def quize():
    sub = None
    right = 0
    wrong = 0
    OS = data['os']

    a = input("\nEnter subject you want to attempt quize \n1.OPP's\n2.DBMS\n3.OS\nYour Ans: ")

    if a == '1' or a == "OPP's":
        sub = OPPS
    elif a == '2' or a == "DBMS":
        sub = DSA
    elif a == '3' or a == "OS":
        sub = OS  
    else:
        print("please give proper input and try again")
        return quize()

    for i in range(5):
        ran_no = str(random.randint(1,10))

        print(f"\n{i+1}.{sub[ran_no][0]}\n")
        print(f"A){sub[ran_no][1][0]}")
        print(f"B){sub[ran_no][1][1]}")
        print(f"C){sub[ran_no][1][2]}")
        print(f"D){sub[ran_no][1][3]}\n")

        ans = check()
        if (sub[ran_no][1][ans]) == (sub[ran_no][2]):
            right += 1
        else:
            wrong += 1

        print("right =",right,", wrong =",wrong)
    return [right,wrong]


def score(r,w):
    print(f"\nNo. of right Ans : {r}")
    print(f"No. of wrong Ans : {w}")
    print(f"\nYour score : {(r/5)*100}\n")

def registration():
    a= input("/nif you doesn't want to register press 's' otherwise press : ")
    if a == 's':
        return

    name = input("please enter your name : ")
    email = input("please enter your email : ")
    user = input("please create username : ")
    passwd = input("please create password : ")
    print("Registration successful!")


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



