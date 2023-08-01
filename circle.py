class Circle:
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        print("Area : ",3.14*(self.radius**2))

c=Circle(int(input("Enter Radius: ")))
c.area()