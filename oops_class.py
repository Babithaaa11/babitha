#class declaration
class Person:
    def print_name(self,name):
        print("my name is" +name)
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b

#object creation
person = Person()
#calling the method
person.print_name("shiva")
result = person.add(3,5)
result1 = person.sub(3,5)
print(result)
print(result1)