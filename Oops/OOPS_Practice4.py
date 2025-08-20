class restaurant:
    def __init__(self,itemcost_1,itemcost_2,itemcost_3,itemcost_4,):
        self.itemcost_1 = itemcost_1
        self.itemcost_2 = itemcost_2
        self.itemcost_3 = itemcost_3
        self.itemcost_4 = itemcost_4
        print("Welcome")
    def Total_bill(self):
        x = (self.itemcost_1 + self.itemcost_2 + self.itemcost_3 + self.itemcost_4)
        return f"Your total Bill is {x}"
     

    
Customer_1 = restaurant(350,400,340,0)
print(Customer_1.itemcost_1,Customer_1.itemcost_2,Customer_1.itemcost_3,Customer_1.itemcost_4)
print(Customer_1.Total_bill())


Customer_2 = restaurant(130,560,140,850)
print(Customer_2.itemcost_1,Customer_2.itemcost_2,Customer_2.itemcost_3,Customer_2.itemcost_4)
Customer_2 = restaurant(130,560,140,850)
print(Customer_2.Total_bill())
