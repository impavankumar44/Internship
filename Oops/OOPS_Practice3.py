#Mini.Project_1
class Circle:
    def __init__(self,radius):
        self.radius = radius
        print("Circles is an Important and interesting concept in Geometry")

    def Area(self):
        return ((self.radius**2)*3.14)
    def Perimeter(self):
        return ((self.radius*3.14)*2)
Cir_1 = Circle(47)
print(Cir_1.Area())
print(Cir_1.Perimeter())
#Mini.Project_2
class Employ:
    def __init__(self,Role,Department,Salary):
        self.Role = Role
        self.Department = Department
        self.Salary = Salary
    def ShowDetails(self):
        print("Role :" , self.Role)
        print("Department :" , self.Department)
        print("Salary" , self.Salary)
class Engineer(Employ):
    def __init__(self,Name, Age):
        super().__init__("Engineer","VLSI Design",120000)
        self.Name = Name
        self.Age = Age
    def ShowDetails(self):
        print("Name :", self.Name , "Age :" , self.Age)
        super().ShowDetails()
        
        

Person_1 = Engineer( "Donald Trump" , 75)
Person_1.ShowDetails()
        
#mini project 3
class order:
    def __init__(self,itemname,price):
        self.itemname = itemname
        self.price = price
    def __get__(item_1,item_2):
        if item_1.price > item_2.price :
            print("price_1 > price_2")
        elif item_1.price < item_2.price :
            print("price_2 > price_1")


item_1 = order("Salt",120)
item_2 = order("Ice cream",180)
item_1.__get__(item_2)