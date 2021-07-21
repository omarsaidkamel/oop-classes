# Create parent Class (Shape)
class Shape:

    # Declare private variable
    __base = 0
    __height = 0
    __length = 0
    __width = 0

    # Create Set function fill the private value
    def set_values(self, width, height):
        self.__width = width
        self.__height = height

    # Create get function to take the value of width
    def get_width(self):
        return self.__width

    # Create get function to take the value of height
    def get_height(self):
        return self.__height

    # Create function To print (area)
    def GetArea(self):
        print('Area: ')


# Create Child Class (Triangle) & inherit from the parent Class (Shape)
class Triangle(Shape):
    # Create function To return the area of Triangle
    def GetArea(self):
        return 0.5 * self.get_width() * self.get_height()


# Create Child Class (Rectangle) & inherit from the parent Class (Shape)
class Rectangle(Shape):
    # Create function To return the area of Rectangle
    def GetArea(self):
        return self.get_width() * self.get_height()


# object of Class Triangle
tArea = Triangle()

# object of Class Triangle
rArea = Rectangle()

# set value of Width & height of triangle
tArea.set_values(10, 20)

# set value of Width & height of Rectangle
rArea.set_values(5, 2)

# print the Area of rectangle
print(rArea.GetArea())

# print the Area of Triangle
print(tArea.GetArea())
