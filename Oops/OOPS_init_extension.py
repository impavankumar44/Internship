class Mark_Analysis:
    def __init__(self,subject_1,subject_2,subject_3):
        self.subject_1 = subject_1
        self.subject_2 = subject_2
        self.subject_3 = subject_3
        print("Students here is your mark analysis")

    def Averages(self):
        x = (self.subject_1 + self.subject_2 + self.subject_3)/3
        return f"This is your Average {x}"
        

student_pranav = Mark_Analysis(98,89,78)
print(student_pranav.subject_1,student_pranav.subject_2,student_pranav.subject_3)
print(student_pranav.Averages())



