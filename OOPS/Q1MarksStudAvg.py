class Student:
     
     def __init__(self,name,marks1,marks2,marks3):
          self.name=name 
          self.physics=marks1
          self.chem=marks2
          self.maths=marks3

     def avg(self):
            print("Average:",(self.physics+self.chem+self.maths)/3)

s1=Student("Peter",96.3,94,98.7)
print(s1.name)
print("Physics",s1.physics)
print("Chemistry",s1.chem)
print("Maths",s1.maths)
s1.avg()
