
f = open("C:\\Mywork\\Filehandling\\File_Handling_dup1.txt","r")
data = f.read(12)
print(data)
f.close()


x = open("C:\\Mywork\\Filehandling\\File_Handling_dup1.txt","a")
x.write("I am working for a period of 3 weeks \n Today I have recieved my ID card.")
x.close()
