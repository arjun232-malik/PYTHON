class Student:
     
     def __init__(self,fullname,marks):
          self.name=fullname 
          self.marks=marks
          # self.physics=marks1
          # self.chem=marks2
          # self.maths=marks3

     def avg(self):
            sum=0
            for i in self.marks:
                  sum+=i
            print(self.name,"'s average score is ",sum/3)   

s1=Student("Peter Parker",[96,94,98])
s1.avg()

s1.name="Spider-man"
s1.avg()
# print(s1.name)
# print("Physics",s1.physics)
# print("Chemistry",s1.chem)
# print("Maths",s1.maths)
# s1.avg()
