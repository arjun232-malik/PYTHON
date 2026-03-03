class Person:
    name="anonymous"

    # def changename(self,name):
    #     # self.name=name
    #     # Person.name=name # class atrr has changed
    #       self.__class__.name="Siddharth Malik"

    @classmethod #decorator
    def changename(cls,name):
        cls.name=name

p1=Person()
p1.changename("Siddharth Malik")
print(p1.name)
print(Person.name)