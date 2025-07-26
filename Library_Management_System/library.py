class Library:

    def borrow(self):
        self.name=input("Enter your name: ")
        self.roll=int(input("Enter you roll no: "))
        self.mobile=int(input("Enter your mobile no: "))
        self.add=input("Enter your address: ")
        self.branch=input("Enter your branch: ")
        self.year=input("Enter your year: ")


        with open("books.txt") as f:
            self.a=f.read()
            print(self.a)

        self.a = input("Enter your favourite book: ")

        with open("records.txt", "r") as f:
            count = f.read().count("Record ")

        with open("records.txt", "a") as f:
            f.write(f'''\nRecord {count + 1}
        The name is {self.name}, a {self.year} {self.branch} student.
        The Address is {self.add}.
        The borrowed book name is {self.a}.
        ------------------------------
        ''')

        print("✅ The book has been borrowed successfully.\n")

    def view(self):
        with open("records.txt") as f:
            print("\n📚 All Records:\n")
            a = f.read()
            print(a)

    def exit(self):
        print("\nThank you visiting!!!\n")


class Student(Library):

    def ret(self):
        self.name = input("Enter your name: ")
        self.roll = int(input("Enter you roll no: "))
        self.add = input("Enter your address: ")
        self.branch = input("Enter your branch: ")
        self.year = input("Enter your year:")
        self.a=input(f"Enter the name of the which you want to return: ")

        with open("records.txt", "r") as f:
            count = f.read().count("Record ")

        with open("records.txt", "a") as f:
            f.write(f'''\nRecord {count + 1}
        The name is {self.name}, a {self.year} {self.branch} student.
        The Address is {self.add}.
        The book returned is {self.a}.
        ------------------------------''')

        print("✅ The book has been returned successfully.\n")


print('''
---------------------------------------------------
\t\t\t...WELCOME TO THE LIBRARY...\t\t\t
---------------------------------------------------''')

def library():

    choice=input('''Choose a option:-\n
1.Borrow a Book
2.Return a Book
3.View Records
4.EXIT

Your choice:   ''')
    l = Library()

    s = Student()

    while True:

        match choice:
            case "1":
                l.borrow()
            case "2":
                s.ret()
            case "3":
                l.view()
            case "4":
                l.exit()
                break
            case '_':
                print("❌ Invalid choice. Please try again.")

        a = input("Do you want to continue(yes/no)? ").lower()
        if a == "yes":
            library()
        elif a == "no":
            break
        else:
            print("Invalid Input.")
library()








