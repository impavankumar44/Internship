class Bank_details:

    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def confidential_details(self):
        return self.__acc_pass
    

detail_1 = Bank_details("65621894","QuzKLnJ45")
print(detail_1.confidential_details())
# This output refers to the call of function Confidential details and returns the password i.e
# A private attribute and hence the password is just readable and can't be changed.


