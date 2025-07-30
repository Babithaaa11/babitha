from abc import ABC

class Person():
    cityName = "mumbai"
    def printName(self,name):
        print(name)

class Ashok(Person):
    def printDetails(self):
        print("some messages")

obj = Ashok()
obj.cityName = "new city"
obj.printName("ashok")

class Arun(Person):
    def printDetails(self):
        print("some messages")

obj = Arun()
obj.cityName = "london"
obj.printName("arun")