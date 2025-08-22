class Birds:
    def __init__(self,species):
        self.species = species
        print(f"Birds : {self.species}")
class Parrot(Birds):
    def __init__(self,species,color):
        self.color = color
        print(f"Parrot color : {self.color}")
        super().__init__(species)
Task = Parrot("Macow","Green")
print(Task.species,Task.color) 
# The output gives the string value of Species i.e Macow and colour i.e green.


class Vehical:
    def Start(self):
        print("Starting the Vehical") # The output gives the string value 'Starting the Vehical'

class car(Vehical):
    def Start(self):
        super().Start()
        print("Car engine started")
        
        
Task_2 = car()
print(Task_2.Start())
# The output gives the string value of 'The output gives the string value' 
        

class A:
    def __init__(self):
        print("Init A")
class B(A):
    def __init__(self):
        super().__init__()
        print("Init B")
class C(B):
    def __init__(self):
        super().__init__()
        print("Init C")
Task_3 = C()
print(Task_3)
# Return Mutiple values of respective class i.e Init A Init B Init C



class Person:
    name = "Pavan Kumar"
    def ChangeName(self,name):
        self.name = name
person_1 = Person()
person_1.ChangeName("Ajay Sai")
print(person_1.name)
# Returns the value of changed name 'Ajay Sai'



class Person:
    name = "Pavan Kumar"
    def ChangeName(self,name):
        Person.name = name
Person_1 = Person()
Person_1.ChangeName("Ajay Sai")
print(Person.name)
# Returns the value of changed name 'Ajay Sai'


class Persons:
    name = "Pavan Kuamr"
    def ChangeName(self,name):
        self.__class__.name = name
Per_1 = Persons()
Per_1.ChangeName("Ajay Sai")
# Returns the value 'Ajay Sai'but this data isn't accesable as its a private attribute.

class Persona:
    name = "Pavan Kumar"
    @classmethod
    def ChangeName(cls,name):
        cls.name = name
Pers_1 = Persona()
Pers_1.ChangeName("Ajay Sai")
print(Per_1.name,Persona.name)
# Returns 'Ajay Sai ' Twice as it is called twice.