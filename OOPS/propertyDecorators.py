class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percentage=str((self.phy+self.chem+self.math)/3) + "%"
        
        def chngemarks

s1=Student(98,78,92)
print(s1.percentage)

s1.chem=87
print(s1.chem)
print(s1.percentage)
