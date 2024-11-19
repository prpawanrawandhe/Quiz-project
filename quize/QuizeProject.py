import random

OS = {
    1: [
        "What does an Operating System do?",
        ["Manages hardware and software resources", "Compiles code", "Designs user interfaces", "Executes only binary code"],
        "Manages hardware and software resources"
    ],
    2: [
        "Which of the following is not an operating system?",
        ["Linux", "Windows", "Oracle", "MacOS"],
        "Oracle"
    ],
    3: [
        "What is the main purpose of a process scheduler?",
        ["To manage system memory", "To allocate CPU time to processes", "To compile programs", "To handle I/O operations"],
        "To allocate CPU time to processes"
    ],
    4: [
        "Which of the following is an example of a real-time operating system?",
        ["Windows 10", "Linux Mint", "VxWorks", "Ubuntu"],
        "VxWorks"
    ],
    5: [
        "What is a deadlock in OS?",
        ["A situation where processes are stuck waiting for resources", "A virus attack on the OS", 
         "An error in booting", "A process that is in an infinite loop"],
        "A situation where processes are stuck waiting for resources"
    ],
    6: [
        "What is a kernel in an operating system?",
        ["The core part of the OS managing system resources", "A user interface", 
         "A type of programming language", "A debugging tool"],
        "The core part of the OS managing system resources"
    ],
    7: [
        "Which of the following scheduling algorithms is non-preemptive?",
        ["Round Robin", "Shortest Job First (SJF)", "Priority Scheduling", "First Come First Serve (FCFS)"],
        "First Come First Serve (FCFS)"
    ],
    8: [
        "What is the role of a device driver in an OS?",
        ["To manage and control hardware components", "To optimize memory usage", 
         "To translate programming code", "To monitor system performance"],
        "To manage and control hardware components"
    ],
    9: [
        "Which type of memory is directly accessible by the CPU?",
        ["RAM", "Cache", "Hard Disk", "Virtual Memory"],
        "Cache"
    ],
    10: [
        "What is virtual memory in an OS?",
        ["A storage area in the hard disk acting as RAM", "A type of physical memory", 
         "An OS-specific application", "An external storage device"],
        "A storage area in the hard disk acting as RAM"
    ]
}

DSA = {
    1: [
        "What does DBMS stand for?",
        ["Database Management System", "Data Backup Management System", "Database Manipulation Software", "Database Monitoring System"],
        "Database Management System"
    ],
    2: [
        "Which of the following is not a type of database?",
        ["Relational", "Hierarchical", "Network", "Flat-tree"],
        "Flat-tree"
    ],
    3: [
        "Which of these is a valid example of a relational database?",
        ["MySQL", "HTML", "Python", "Excel"],
        "MySQL"
    ],
    4: [
        "What is the main function of a primary key in a database?",
        ["To uniquely identify a record", "To create relationships between tables", "To store foreign keys", "To store metadata"],
        "To uniquely identify a record"
    ],
    5: [
        "Which of the following is a DDL (Data Definition Language) command?",
        ["SELECT", "INSERT", "UPDATE", "CREATE"],
        "CREATE"
    ],
    6: [
        "Which command is used to remove a table from a database?",
        ["DROP", "DELETE", "TRUNCATE", "REMOVE"],
        "DROP"
    ],
    7: [
        "What is the purpose of the ACID properties in DBMS?",
        ["To ensure data security", "To maintain data integrity during transactions", "To enhance database speed", "To backup data"],
        "To maintain data integrity during transactions"
    ],
    8: [
        "Which of the following is an example of a NoSQL database?",
        ["MongoDB", "PostgreSQL", "Oracle", "SQLite"],
        "MongoDB"
    ],
    9: [
        "What is a foreign key used for?",
        ["To enforce referential integrity", "To uniquely identify records", "To execute queries", "To increase performance"],
        "To enforce referential integrity"
    ],
    10: [
        "Which of these is a constraint in a relational database?",
        ["NOT NULL", "ORDER BY", "SELECT", "JOIN"],
        "NOT NULL"
    ]
}

OPPS  = {
    1: [
        "What does OOP stand for?",
        ["Object-Oriented Programming", "Object-Oriented Processing", "Object-Oriented Principles", "Object-Oriented Paradigm"],
        "Object-Oriented Programming"
    ],
    2: [
        "Which of the following is not a principle of OOP?",
        ["Encapsulation", "Polymorphism", "Abstraction", "Compilation"],
        "Compilation"
    ],
    3: [
        "Which feature of OOP indicates code reuse?",
        ["Encapsulation", "Inheritance", "Polymorphism", "Abstraction"],
        "Inheritance"
    ],
    4: [
        "What is used to define a blueprint for objects in OOP?",
        ["Function", "Class", "Method", "Module"],
        "Class"
    ],
    5: [
        "Which of the following best defines polymorphism?",
        ["Using multiple methods with the same name", "Using multiple classes in a program", "Changing object state", "Hiding data"],
        "Using multiple methods with the same name"
    ],
    6: [
        "Which OOP concept is used to achieve runtime polymorphism?",
        ["Inheritance", "Overloading", "Overriding", "Encapsulation"],
        "Overriding"
    ],
    7: [
        "What is encapsulation in OOP?",
        ["Combining data and functions into a single unit", "Restricting access to some components of an object", 
         "Using inheritance for code reuse", "None of the above"],
        "Restricting access to some components of an object"
    ],
    8: [
        "Which of the following is an example of an abstract data type?",
        ["String", "Class", "Interface", "Object"],
        "Interface"
    ],
    9: [
        "What keyword is used to create a subclass in Python?",
        ["class", "subclass", "inherit", "extends"],
        "class"
    ],
    10: [
        "Which of the following is a special method in Python classes?",
        ["__init__", "main()", "__str__", "All of the above"],
        "__init__"
    ]
}





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
        ran_no = random.randint(1,10)

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


def welcome():
    print("\n~ WELCOME TO QUIZE ROUNDS ~")
    login()
    a = quize()
    score(a[0],a[1])


welcome()


