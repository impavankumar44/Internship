#Mini.Project_1
class Circle:

    def __init__(self,radius):
        self.radius = radius
        print("Circles is an Important and interesting concept in Geometry")
        # The output returns the string value that is 
        # 'Circles is an Important and interesting concept in Geometry'

    def area(self):
        return ((self.radius**2)*3.14)
    
    def perimeter(self):
        return ((self.radius*3.14)*2)
    

cir_1 = Circle(47)
print(cir_1.area()) # This output returns the integer that gives the area of the circle of radius 47
print(cir_1.perimeter()) 
# This output returns the integer that gives the  perimeter of the circle of radius 47
# Mini.Project_2


class Employ:

    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showdetails(self):
        print("Role :" , self.role)
        print("Department :" , self.department)
        print("Salary" , self.salary)


class Engineer(Employ):

    def __init__(self,name, age):
        super().__init__("Engineer","VLSI Design",120000)
        self.name = name
        self.age = age

    def showdetails(self):
        print("Name :", self.name , "Age :" , self.age)
        super().showdetails()
        
        
person_1 = Engineer( "Donald Trump" , 75)
person_1.showdetails()
# Here the ShowDetails function is called and it returns a set of information i.e 
# Name , age and Role , Department salary 

        
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