# import os
# phison = open("fileIO.py", 'wb')
# print ("Name of the file: ", phison.name)
# print ("Closed or not : ", phison.closed)
# print ("Opening mode : ", phison.mode)
# print ("Softspace flag : "), phison.softspace


class Person:
    def __init__(self, name, age, sex):
        self.name = name    
        self.age = age
        self.sex = sex

    def fc1(self):
        print("My name is"+ self.name  + self.sex )
        print(self.age)
p1 = Person("Phi Son",24, "bede")
p1.fc1()
p1.age = 40
p1.fc1()