class Bank_balance:

    def __init__(self,account_no,balance):
        self.account_no =  account_no
        self.balance = balance

    def transaction(self):
        x = int(input())#Amount credited
        y = int(input())#Ammount debited
        z = (self.balance + x - y)
        return f"The Final amount on your bank account is {z}"
    

account_1 = Bank_balance(int(8425),int(85000))
print(account_1.account_no,account_1.balance)
# Returns the data type int that gives the value of 'Account number' and 'Account Balance'
print(account_1.transaction())
# This output returns the value of Balance left after money is credited and debited that we are supposed to 
# Give the input value of money credited and money debited