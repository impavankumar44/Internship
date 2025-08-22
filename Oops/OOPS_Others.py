# Hybrid Inheritance.
class ZP_High_School:
    Principal = " Principal : Sathya ,"
    HM = " HM : Nritya ,"

class ZP_Class_10(ZP_High_School):
    Maths_Teacher = "Maths Teacher : Vidhya ,"
    Chem_Teacher = " Chem Teacher : Tehmina ," 
    
class ZP_Class_9(ZP_High_School):
    Social = "Social Teacher : Gopi ,"
    PT = "PT : Deepu ,"

class ZP_Staff(ZP_Class_10,ZP_Class_9):
    Attender = "Attender : Ramesh ,"
    

Staff_Attendence = ZP_Staff()
print(Staff_Attendence.Principal,Staff_Attendence.HM,
      Staff_Attendence.Maths_Teacher,Staff_Attendence.Chem_Teacher,
      Staff_Attendence.Social,Staff_Attendence.PT,
      Staff_Attendence.Attender)
# The output returns the string value of staff like Principal , HM , Maths teacher ,
# Chemistry teacher , Social teacher , PT and Attender in horizontal form
      

x  = (Staff_Attendence.Principal,Staff_Attendence.HM,
       Staff_Attendence.Maths_Teacher,Staff_Attendence.Chem_Teacher,
       Staff_Attendence.Social,Staff_Attendence.PT,Staff_Attendence.Attender)
for each in x:
    print(each)
# The output returns the string value of staff like Principal , HM , Maths teacher ,
# Chemistry teacher , Social teacher , PT and Attender in vertical form