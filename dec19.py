import pandas as pd
#print(pd.__version__)
class Student:
    def __init__(self):
        print("Inside Student")
        self.name=input("Enter Name: ")
        self.surname = input("Enter surname: ")
        self.year_of_birth = input("Enter year_of_birth: ")
        self.clss = input("Enter clss: ") 
class School(Student):
    def __init__(self,*args):        
        super().__init__(*args)      
        self.schoolname = input("Enter schoolname: ")
    def __str__(self):
        return self.name + self.surname +self.year_of_birth +self.clss +self.schoolname    

no_of_students = int(input("Enter no. of students"))
x=[]
for i in range(no_of_students):
    school_obj=School()
    x.append(school_obj)
pd.DataFrame.from_records(s.__dict__ for s in x)
       