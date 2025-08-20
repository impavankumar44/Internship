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


class Vehical:
    def Start(self):
        print("Starting the Vehical")

class car(Vehical):
    def Start(self):
        super().Start()
        print("Car engine started")
        
Task_2 = car()
print(Task_2.Start())
        

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



class Person:
    name = "Pavan Kumar"
    def ChangeName(self,name):
        self.name = name
person_1 = Person()
person_1.ChangeName("Ajay Sai")
print(person_1.name)



class Person:
    name = "Pavan Kumar"
    def ChangeName(self,name):
        Person.name = name
Person_1 = Person()
Person_1.ChangeName("Ajay Sai")
print(Person.name)


class Persons:
    name = "Pavan Kuamr"
    def ChangeName(self,name):
        self.__class__.name = name
Per_1 = Persons()
Per_1.ChangeName("Ajay Sai")

class Persona:
    name = "Pavan Kumar"
    @classmethod
    def ChangeName(cls,name):
        cls.name = name
Pers_1 = Persona()
Pers_1.ChangeName("Ajay Sai")
print(Per_1.name,Persona.name)