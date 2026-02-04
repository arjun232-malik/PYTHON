class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3) + "%"

s1=Student(98,78,92)
print(s1.percentage)

s1.chem=87
print(s1.percentage)
