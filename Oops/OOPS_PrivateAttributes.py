class Bank_Details:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    def Confidential_details(self):
        return self.__acc_pass

Detail_1 = Bank_Details("65621894","QuzKLnJ45")
print(Detail_1.Confidential_details())


