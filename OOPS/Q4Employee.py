class Employee:

    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    
    def showDetails(self):
        print("Your role will be",self.role,"in the department",self.dept,"and your salary will be",self.salary)

class Engineer(Employee):
     def __init__(self,name,age):
         self.name=name 
         self.age=age
         super().__init__("Engineer","IT","90,000")     

engr1=Engineer("Arjun",25)  
print("Name",engr1.name)
print("Age",engr1.age)
engr1.showDetails()
