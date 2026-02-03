class Student:
     college_name="Exeter College"
     name="Abhay" #class attr
     
     #parameterized constructor
     def __init__(self,name,age):
          self.name=name #obj attr > class attr
          self.age=age

s1=Student("Siddharth",21)
print(s1.name,s1.age)
s2=Student("Siddhu",20)
print(s1.name,s2.age)

print(Student.college_name)
