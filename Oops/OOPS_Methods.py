class bikes:

    def __init__(self,cost_body,cost_part,cost_taxes,cost_registration):
        self.cost_body = cost_body
        self.cost_part = cost_part
        self.cost_taxes = cost_taxes
        self.cost_registration = cost_registration
        print("Congrats you have bought your dream bike") # This outcome returns the string 'Congrats 
        #you have bought your dream bike'
    def Total_cost(self):
        x = (self.cost_body + self.cost_part + self.cost_taxes + self.cost_registration)
        return f"The total cost of the bike is {x}"
        
    


model_1 = bikes(25000,250000,25000,50000)
print(model_1.cost_body,model_1.cost_part,model_1.cost_taxes,model_1. cost_registration)
# The outcome returns the string that gives the value of cost of body , parts and amount that are charged 
# as tax and registration
print(model_1.Total_cost())
model_2 = bikes(95000,525000,125000,50000)

print(model_2.cost_body,model_2.cost_part,model_2.cost_taxes,model_2.cost_registration)
print(model_2.Total_cost())
# The outcome returns the string that gives the value of cost of body , parts and amount that are charged 
# as tax and registration


    