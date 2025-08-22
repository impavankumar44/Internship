class Mark_analysis:

    def __init__(self,subject_1,subject_2,subject_3):
        self.subject_1 = subject_1
        self.subject_2 = subject_2
        self.subject_3 = subject_3
        print("Students here is your mark analysis")
        # The output returns the string 'Students here is your mark analysis'

    def averages(self):
        x = (self.subject_1 + self.subject_2 + self.subject_3)/3
        return f"This is your Average {x}"
        

student_pranav = Mark_analysis(98,89,78)
print(student_pranav.subject_1,student_pranav.subject_2,student_pranav.subject_3)
# The output returns the marks of students 
print(student_pranav.averages())
# The output returns the average of students , marks



