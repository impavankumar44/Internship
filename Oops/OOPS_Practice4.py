class Restaurant:

    def __init__(self,itemcost_1,itemcost_2,itemcost_3,itemcost_4,):
        self.itemcost_1 = itemcost_1
        self.itemcost_2 = itemcost_2
        self.itemcost_3 = itemcost_3
        self.itemcost_4 = itemcost_4
        print("Welcome") # Returns the string value 'Welcome'

    def total_bill(self):
        x = (self.itemcost_1 + self.itemcost_2 + self.itemcost_3 + self.itemcost_4)
        return f"Your total Bill is {x}"

    
customer_1 = Restaurant(350,400,340,0)
print(customer_1.itemcost_1,customer_1.itemcost_2,customer_1.itemcost_3,customer_1.itemcost_4)
# The output returns the cost of items in the restaurant
print(customer_1.total_bill())
# The output returns the total cost for what the perticualr customer has consumed 


customer_2 = Restaurant(130,560,140,850)
print(customer_2.itemcost_1,customer_2.itemcost_2,customer_2.itemcost_3,customer_2.itemcost_4)
# The output returns the cost of items in the restaurant
print(customer_2.total_bill())
# # The output returns the total cost for what the perticualr customer has consumed 
