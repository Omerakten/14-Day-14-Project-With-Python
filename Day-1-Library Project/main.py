Red = "\u001b[31m"
Green="\u001b[32m"
Yellow="\u001b[33m"
Magenta="\u001b[35m"
Cyan = "\u001b[36m"
White = "\u001b[37m"
Black = "'\u001b[30m"



print(f"{Green}███████████████████████████████████████████████████████████████████████")
print(f"{Green}███████████████████{Yellow}New York City Library{Green}█████████████████████")
print(f"{Green}███████████████████████████████████████████████████████████████████████")
print(f"{Cyan}")
import random

class Login:
    def __init__(self,username,password):
        self.username = username
        self.password = password

log = Login("user","123456")

class App:
    def __init__(self,title):
        self.title = title
        self.control()
        self.dongu = True

    def control(self):
        count = 2

        for i in range(0, 3):
            username = str(input("Please enter your username:\n"))
            password = str(input("please enter your password:\n"))

            if username == log.username and password == log.password:
                print("███████████████████████████████████████████████████████████████████████")
                print(f"{Red}Login successful{Cyan}")
                print("███████████████████████████████████████████████████████████████████████")
                print("New York City Library")
                self.program()
                break
            elif username != log.username or password != log.password and count != 0:
                print("Incorrect, Try Again Counter:{}".format(count))
                count -= 1

            if count == -1:
                print("System is shutting down..".format(count))
                exit()

    def program(self):

        act = self.menu()
        if act == 1:
            self.allBooks()
        if act == 2:
            self.allMember()
        if act == 3:
            self.addBook()
        if act == 4:
            self.removeBook()
        if act == 5:
            self.addMember()
        if act == 6:
            self.removeMember()
        if act == 7:
            self.giveBook()
        if act == 8:
            self.takeBook()
        if act == 9:
            self.givenBookList()
        if act == 10:
            self.takenBookList()
        if act == 11:
            self.shutDown()

    def menu(self):
        print("███████████████████████████████████████████████████████████████████████")
        act = int(input("Please Select Action\n"
                        "1- All Books\n"
                        "2- All Members\n"
                        "3- Add Book\n"
                        "4- Remove Book\n"
                        "5- Add Member\n"
                        "6- Remove Member\n"
                        "7- Give Book\n"
                        "8- Take Book\n"
                        "9- Given Book List\n"
                        "10-Taken Book List\n"
                        "11- System Shut Down\n"
                        "Select: "))
        print("███████████████████████████████████████████████████████████████████████")

        while act <1 or act>11:
            print("███████████████████████████████████████████████████████████████████████")
            print("\nPlease select only 1- 11\n")
            print("███████████████████████████████████████████████████████████████████████")
            self.program()
        return act

    def allBooks(self):
        print("█████████████████████████████ All Books ███████████████████████████████")
        with open("allbooks.txt","r",encoding="utf-8") as books:
            books.seek(0)
            lineSize = len(books.readlines())
            print("Number of books in the library: {}".format(lineSize))

        with open("allbooks.txt","r",encoding="utf-8") as books:
            books.seek(0)
            print(books.read())

        self.menuReturn()

    def allMember(self):
        print("█████████████████████████████ All Members ██████████████████████████████")
        with open("allmembers.txt","r",encoding="utf-8") as members:
            members.seek(0)
            lineSize = len(members.readlines())
            print("Number of Members in the library: {}".format(lineSize))
        with open("allmembers.txt","r",encoding="utf-8") as members:
            members.seek(0)
            print(members.read())
        self.menuReturn()

    def addBook(self):
            with open("allbooks.txt","a+", encoding="utf-8") as book:
                randGen = random.SystemRandom()
                id = randGen.randint(11111111, 99999999)
                print("█████████████████████████████ Add Book ██████████████████████████████")
                bookName = str(input("Please enter the book name:\n"))
                bookAuthor = str(input("Please enter author name:\n"))
                book.write("{} || Book Name:{} || Book Author: {}\n".format(id,bookName,bookAuthor))
                with open("allbookstable.txt", "a+", encoding="utf-8") as stable:
                    stable.write("{} || Book Name:{} || Book Author: {}\n".format(id, bookName, bookAuthor))


            loop = True
            while loop:
                print("███████████████████████████████████████████████████████████████████████")
                x = int(input("Again Add Book > 1\n"
                              "Continue > 2\n"
                              "Select: "))
                print("███████████████████████████████████████████████████████████████████████")
                if x == 1:
                    self.addBook()
                if x == 2:
                    self.menuReturn()
                if x != 1 and x != 2:
                    print("Please only 1-2")
                    loop == False

    def removeBook(self):
        with open("allbooks.txt", "r", encoding="utf-8") as books:
            allbooks = books.readlines()
            print("█████████████████████████████ All Books ██████████████████████████████")
            print("".join(allbooks))
        print("███████████████████████████████████████████████████████████████████████")
        removeId = input("Enter the ID number of the record you want to delete: \n")

        with open("allbooks.txt", "w", encoding="utf-8") as books:
            for book in allbooks:
                if removeId not in book:
                    books.write(book)

        with open("allbookstable.txt", "w", encoding="utf-8") as stable:
            for book in allbooks:
                if removeId not in book:
                    stable.write(book)

        print("Selected book is removed from the list.\n")
        print("█████████████████████████████ All Books ██████████████████████████████")
        with open("allbooks.txt", "r", encoding="utf-8") as books:
            books.seek(0)
            print(books.read())

        loop = True
        while loop:
            print("███████████████████████████████████████████████████████████████████████")
            x = int(input("Again Remove Book > 1\n"
                          "Continue > 2\n"
                          "Select: "))
            print("███████████████████████████████████████████████████████████████████████")
            if x == 1:
                self.addBook()
            if x == 2:
                self.menuReturn()
            if x != 1 and x != 2:
                print("Please only 1-2")
                loop == False

    def addMember(self):
        with open("allmembers.txt", "a+", encoding="utf-8") as member:
            randGen = random.SystemRandom()
            id = randGen.randint(111111111, 999999999)
            print("█████████████████████████████ Add Member ██████████████████████████████")
            memberName = str(input("Please enter the Name: \n"))
            memberSurname = str(input("Please enter the Surname: \n"))
            memberAge = str(input("Please enter the Age: \n"))
            memberBirthDay = str(input("Please enter the Birthday: \n"))
            memberCity = str(input("Please enter the City: \n"))
            member.write("{} || Name: {} || Surname: {} || Age: {} || Birthday: {} || City: {}\n".format(id, memberName, memberSurname,memberAge,memberBirthDay,memberCity))
        loop = True
        while loop:
            print("███████████████████████████████████████████████████████████████████████")
            x = int(input("Again Add Member > 1\n"
                          "Continue > 2\n"
                          "Select: "))
            print("███████████████████████████████████████████████████████████████████████")
            if x == 1:
                self.addMember()
            if x == 2:
                self.menuReturn()
            if x != 1 and x != 2:
                print("Please only 1-2")
                loop == False

    def removeMember(self):
        with open("allmembers.txt", "r", encoding="utf-8") as member:
            allmember = member.readlines()
            print("█████████████████████████████ All Member ██████████████████████████████")
            print("".join(allmember))
        print("███████████████████████████████████████████████████████████████████████")
        removeId = input("Enter the ID number of the record you want to delete: \n")

        with open("allmembers.txt", "w", encoding="utf-8") as members:
            for member in allmember:
                if removeId not in member:
                    members.write(member)
        print("Selected book is removed from the list.\n")
        print("███████████████████████████████████████████████████████████████████████")
        with open("allmembers.txt", "r", encoding="utf-8") as member:
            allmember = member.readlines()
            print("█████████████████████████████ All Member ██████████████████████████████")
            print("".join(allmember))

        loop = True
        while loop:
            print("███████████████████████████████████████████████████████████████████████")
            x = int(input("Again Remove Member > 1\n"
                          "Continue > 2\n"
                          "Select: "))
            print("███████████████████████████████████████████████████████████████████████")
            if x == 1:
                self.removeMember()
            if x == 2:
                self.menuReturn()
            if x != 1 and x != 2:
                print("Please only 1-2")
                loop == False

    def giveBook(self):
        with open("allbooks.txt", "r", encoding="utf-8") as book:
            allbook = book.readlines()
            allbook_str = "".join(allbook)
            print("█████████████████████████████ All Books ██████████████████████████████")
            print(allbook_str)
        print("███████████████████████████████████████████████████████████████████████")
        givenBook = input("Enter the ID number of the record you want to given book: \n")
        print("███████████████████████████████████████████████████████████████████████")
        with open("allmembers.txt", "r", encoding="utf-8") as member:
            allmember = member.readlines()
            allmember_str = "".join(allmember)
            print("█████████████████████████████ All Members ██████████████████████████████")
            print(allmember_str)
        print("███████████████████████████████████████████████████████████████████████")
        givenMember = input("Enter the ID number of the record you want to given member: \n")
        print("███████████████████████████████████████████████████████████████████████")
        with open("givebook.txt", "a+", encoding="utf-8") as give:
            for book in allbook:
                if givenBook in book:
                    give.write(book.rstrip('\n') + " >>>>>> ")
            for member in allmember:
                if givenMember in member:
                    give.write(member.rstrip('\n'))

            give.write("\n")

        with open("allbooks.txt", "w", encoding="utf-8") as books:
            for book in allbook:
                if givenBook not in book:
                    books.write(book)
            print("███████████████████████████████████████████████████████████████████████")
            print("This book has been removed from the books list")
            print("███████████████████████████████████████████████████████████████████████")

        with open("givebook.txt","r",encoding="utf-8") as given:
            givee = given.readlines()
            print("█████████████████████████████ Given Books ██████████████████████████████")
            print("".join(givee))

        loop = True
        while loop:
            print("███████████████████████████████████████████████████████████████████████")
            x = int(input("Again Give Book > 1\n"
                          "Continue > 2\n"
                          "Select: "))
            print("███████████████████████████████████████████████████████████████████████")
            if x == 1:
                self.giveBook()
            if x == 2:
                self.menuReturn()
            if x != 1 and x != 2:
                print("Please only 1-2")
                loop == False

    def takeBook(self):
        with open("givebook.txt", "r", encoding="utf-8") as givenbooks:
            given = givenbooks.readlines()
            print("█████████████████████████████ Given Books & Member ██████████████████████████████")
            print("".join(given))
        with open("allbookstable.txt", "r", encoding="utf-8") as stablebook:
            stable = stablebook.readlines()

        print("███████████████████████████████████████████████████████████████████████")
        givenBook = input("Enter the ID number of the record you want to taken book: \n")
        print("███████████████████████████████████████████████████████████████████████")
        with open("givebook.txt","a+",encoding="utf-8"):
            for book in given:
                if givenBook in book:
                    with open("takenbook.txt", "a+", encoding="utf-8") as taken:
                        taken.write(book)

        with open("allbookstable.txt", "a+", encoding="utf-8"):
            for books in stable:
                if givenBook in books:
                    with open("allbooks.txt", "a+", encoding="utf-8") as taken:
                        taken.write(books)

        with open("givebook.txt", "w", encoding="utf-8") as books:
            for book in given:
                if givenBook not in book:
                    books.write(book)
            print("This book has been removed from the books list.")
            print("███████████████████████████████████████████████████████████████████████")


        with open("takenbook.txt","r",encoding="utf-8") as taken:
            takee = taken.readlines()
            print("█████████████████████████████ Taken Books ██████████████████████████████")
            print("".join(takee))

        loop = True
        while loop:
            print("███████████████████████████████████████████████████████████████████████")
            x = int(input("Again Take Book > 1\n"
                          "Continue > 2\n"
                          "Select: "))
            print("███████████████████████████████████████████████████████████████████████")
            if x == 1:
                self.takeBook()
            if x == 2:
                self.menuReturn()
            if x != 1 and x != 2:
                print("Please only 1-2")
                loop == False
    def shutDown(self):
        self.dongu = False
        print("███████████████████████████████████████████████████████████████████████")
        print("██████████████████████ System Shut Down! ██████████████████████████████")
        print("███████████████████████████████████████████████████████████████████████")
        exit()
    def takenBookList(self):
        with open("takenbook.txt", "r", encoding="utf-8") as take:
            take.seek(0)
            lineSize = len(take.readlines())
            print("███████████████████████████████████████████████████████████████████████")
            print("Number of taken books in the library: {}".format(lineSize))

        with open("takenbook.txt", "r", encoding="utf-8") as take:
            take.seek(0)
            print(take.read())
        self.menuReturn()
    def givenBookList(self):
        with open("givebook.txt", "r", encoding="utf-8") as give:
            give.seek(0)
            lineSize = len(give.readlines())
            print("███████████████████████████████████████████████████████████████████████")
            print("Number of books in the library: {}".format(lineSize))

        with open("givebook.txt", "r", encoding="utf-8") as give:
            give.seek(0)
            print(give.read())
        self.menuReturn()
    def menuReturn(self):
        print("███████████████████████████████████████████████████████████████████████")
        x = int(input("To return to the main menu > 1\n"
                      "To Exit the System > 2\n"
                      "Select: "))
        print("███████████████████████████████████████████████████████████████████████")
        if x == 1:
            self.program()
        if x == 2:
            self.shutDown()
        if x != 1 and x != 2:
            print("Please only 1-2")
            self.menuReturn()
app = App("New York City Library")
while app.dongu:
    app.program()