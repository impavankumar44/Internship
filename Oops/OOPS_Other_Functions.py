class car:
    def __init__(self,model,colour):
        self.model = model
        self.colour = colour

    @staticmethod
    def name_customer():
          print("Ford Mustang")
Customer_1 = car("Pavan","Black")
print(Customer_1.model,Customer_1.colour)
# The output returns the value of model and colour of car that the customer_1 has bought.
Customer_1.name_customer()



print("Delete Function") # The output returns the value 'Delete Function'

class password:
     def __init__(self,words,number):
          self.words = words
          self.number = number


pass_1 = password("PshuId","89545")
del pass_1

print(pass_1.words,pass_1.number)
#get error as the function is deleted