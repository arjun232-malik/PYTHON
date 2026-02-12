class Circle:

    def __init__(self,radius):
        self.radius=radius

    def Area(self):
        return (self.radius**2)*3.14
    
    def perimeter(self):
        return 2*(3.14)*self.radius

c1=Circle(6)
print("Area of the circle is",c1.Area(),"cmsq")
print("Perimeter of the circle is",c1.perimeter(),"cm")
