class Student:
     college_name="Exeter College"
     
     def __init__(self,name,marks):
          self.name=name 
          self.marks=marks

     def welcome(self):
          print("welcome new student,",self.name)

     def marks_get(self):
          return self.marks       

s1=Student("Arjun",94.6)
s1.welcome()
print(s1.marks_get())