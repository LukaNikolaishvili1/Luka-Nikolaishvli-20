        #savarjisho 1

# class People:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#
#     def get_email(self):
#         return f"{self.firstname}.{self.lastname}.uni@btu.edu.ge"
#
# class Lecturer(People):
#     def __init__(self, firstname, lastname, salary):
#         super().__init__(firstname, lastname)
#         self.salary = salary
#
#     def get_email(self):
#         return f"{self.firstname}.{self.lastname}@btu.edu.ge"
#
# class Student(People):
#     def __init__(self, firstname, lastname, courses):
#         super().__init__(firstname, lastname)
#         self.courses = courses
#
#     def get_email(self):
#         return f"{self.firstname}.{self.lastname}.1@btu.edu.ge"
#
# s1 = Student("jemala", "zambaxadze", ["python", "C++"])
# l1 = Lecturer("zurabi", "svanadze", 3000)
# p1 = People("LUKA", "NIKOLAISHVILI")
#
# print(s1.get_email())
# print(l1.get_email())
# print(p1.get_email())
#
#


        #savatjisho 3

# class MailSender:
#     def send_mail(self):
#         return 'თქვენი მეილი გაიგზავნა ამ მისამართზე: giorgi.giorgadze@gmail.com'
#
#
#
# class Contacts:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#
# class Friend(Contacts,MailSender):
#     def __init__(self, Name, phone, email):
#         super().__init__(Name,phone)
#         self.email = email
#
# class Family(Contacts,MailSender):
#     def __init__(self, name, phone, email, birthday):
#         super().__init__(name, phone)
#         self.email = email
#         self.birthday = birthday
#
#
# person1 = Friend('gela','giorgadze','gelagiorgadze@gmail.com')
# print(person1.send_mail())



#savarjisho 2
class LibraryItem:
def __init__(self, title, status="xelmisawvdomi"):
self.title = title
self.status = status

def booking(self):
if self.status == "xelmisawvdomi":
self.status = "dakavebuli"
return f"{self.title} warmatebit aris dajavshnili"
else:
return f"{self.title} ukve dajavshnilia"


class Book(LibraryItem):
def __init__(self, title, author, status="xelmisawvdomi"):
super().__init__(title, status)
self.author = author

def booking(self):
return super().booking()


class CD(LibraryItem):
def __init__(self, title, artist, status="xelmisawvdomi"):
super().__init__(title, status)
self.artist = artist

def booking(self):
return "CD dajavshvna ar aris xelmisawvdomi"



book1 = Book("Harry Potter", "zezva")
book2 = Book("The txa", "jemala")
cd1 = CD("Best", "idk")

print(book1.booking())
print(book1.booking())
print(cd1.booking())