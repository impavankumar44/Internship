class marklist:
    def __init__(self,Mathematics,Economics,Electronics):
        self.Mathematics = Mathematics
        self.Economics = Economics
        self.Electronics = Electronics
        print("Welcome to the parent teacher conference")
        # Calls the string 'Welcome to the parent teacher conference'
    def Average(self):
        x = (self.Mathematics + self.Economics + self.Electronics)/3
        return f"Dear parent your ward has scored an average of {x} and that is great"
student_1 = marklist(98,69,85)
print(student_1.Mathematics,student_1.Economics,student_1.Electronics)
# Returns the marks of students in subjects of maths , economics and electronics
print(student_1.Average())
# Returns the Average of all subjects mentioned above
student_2 = marklist(86,58,98)
print(student_2.Mathematics,student_2.Economics,student_2.Electronics)
# Returns the Average of all subjects mentioned above
print(student_2.Average()) 
# Returns the Average of all subjects mentioned above

print("Method 2") # Returns 'Method 2'


class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def Average(self):
        x = (sum(self.marks))/3
        return f"Dear parents hear is the average of your ward {x} and it's a great grade"

student_1 = Student("Pavan Kumar",[98,69,92])
print(student_1.name,student_1.marks)
# The output value returns the value name and marks in subjects in a list.
print(student_1.Average())
# The output value returns the average marks of respective subjects.
student_2 = Student("Praveen",[96,63,69])
print(student_2.name,student_2.marks)
# The output value returns the value name and marks in subjects in a list.
print(student_2.Average())
# The output value returns the average marks of respective subjects.



print("Abstraction") # returns the value 'Abstraction'
class Answer_sheet:
    def __init__(self):
        self.Question_1 = True
        self.Question_2 = True
        self.Question_3 = False
        self.Question_4 = True
    def Recorrection(self):
        self.Question_1 = True
        self.Question_2 = False
        self.Question_3 = False
        self.Question_4 = True
        print("The correction department is clear and transparent about the result")

Student_1 = Answer_sheet()
Student_1.Recorrection()
# Returns the string that tells that student about recorrection 
# 'The correction department is clear and transparent about the result' 