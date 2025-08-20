class Bank_Balance:

    def __init__(self,Account_no,Balance):
        self.Account_no =  Account_no
        self.Balance = Balance
    def Transaction(self):
        x = int(input())#Amount credited
        y = int(input())#Ammount debited
        z = (self.Balance + x - y)
        return f"The Final amount on your bank account is {z}"
Account_1 = Bank_Balance(int(8425),int(85000))
print(Account_1.Account_no,Account_1.Balance)
print(Account_1.Transaction())
