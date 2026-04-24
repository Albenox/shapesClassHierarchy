# A program that uses an abstract parent class and many child classes to hold information of shapes that can be reused, passed through, and edited efficiently

# Abstract base class that holds the basic shape properties and methods
from abc import ABC, abstractmethod
import math

# Abstract, or parent class that holds broad shapes
class BasicShape(ABC):
    
    # Protected instance variables for area and name (by using an underscore after the period) with placeholder blank values so they can still be used without error of not being initialized
    # __init__ is called once when a new object is created, setting the area and name to usable values, which can be changed later by the user
    def __init__(self):
        self._area = 0.0
        self._name = ""
    
    # A property that waits to see if .area is called, and if it is, returns the value of the area, which is a float
    # Properties wait to run until the value is read
    @property
    def area(self):
        return self._area
       
    # A property that waits to see if .name is called, and if it is, returns the value of the name, which is a string
    @property
    def name(self):
        return self._name
        
    # A setter that waits to see if .area is called, and if it is, sets the value of the area to the value given by the user, which is a float
    # Setters wait to run until the value is set
    @area.setter
    def area(self, value):
        # Checks to see if the value given by the user is greater than or equal to 0, since area cannot be negative, and if it is, sets the value of the area to the value given by the user
        if value >= 0:
            self._area = value

    # A setter that waits to see if .name is called, and if it is, sets the value of the name to the value given by the user, which is a string
    @name.setter
    def name(self, value):
        self._name = value

    # An abstract method that is here to ensure child classes have this method to calculate the area, since different shapes will use different formulas to calculate area, it cannot be declared here
    @abstractmethod
    def calc_area(self):
        pass

# A child class that inherits from the BasicShape class, and represents a circle, with properties for the center coordinates and radius, and a method to calculate the area of the circle
class Circle(BasicShape):
    def __init__(self, x, y, r, n = "Circle"):
        # Calls the __init__ method of the parent class to initialize the area and name properties
        super().__init__() 
            
        self._x_center = x  
        self._y_center = y
        self._radius = r
        self.name = n

        # Calls the calc_area method to calculate the area of the circle when the object is created
        self.calc_area() 

    # Property for radius, x_center, and y_center that waits to see if .radius, .x_center, or .y_center is called, and if it is, returns the value of the radius, x_center, or y_center,
    @property
    def radius(self):
        return self._radius

    @property
    def x_center(self):
        return self._x_center

    @property
    def y_center(self):
        return self._y_center

    # Setter for radius, that also recalculates the area when called, and checks for valid input
    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
            # Calls to calc_area to recalculate the area of the circle when the radius is changed
            self.calc_area() 

    def calc_area(self):
        self._area = math.pi * self._radius ** 2

# A child class that inherits from the BasicShape class, and represents a rectangle, with properties for length and width, and a method to calculate the area of the rectangle
class Rectangle(BasicShape):
    def __init__(self, l, w, n = "Rectangle"):
        # Calls the __init__ method of the parent class to initialize the area and name properties
        super().__init__() 
            
        # Protected instance variables for length and width, with placeholder blank values so they can still be used without error of not being initialized
        self._length = l
        self._width = w
        self.name = n
            
        # Calls the calc_area method to calculate the area of the rectangle when the object is created
        self.calc_area() 
        
    # Properties for length and width that wait to see if .length or .width is called, and if it is, returns the value of the length or width
    @property
    def length(self):
        return self._length
            
    @property
    def width(self):
        return self._width
        
    # Setters for length and width that also recalculate the area when called, and checks for valid input
    @length.setter
    def length(self, value):
        if value >= 0:
            self._length = value
            # Calls to calc_area to recalculate the area of the rectangle when the length is changed
            self.calc_area()
        
    @width.setter
    def width(self, value):
        if value >= 0:
            self._width = value
            # Calls to calc_area to recalculate the area of the rectangle when the width is changed
            self.calc_area() 
         
    # A method that calculates the area of the rectangle using the formula length * width, and sets the value of the area property to the calculated area
    def calc_area(self):
        self._area = self._length * self._width

# A child class that inherits from the Rectangle class, and represents a square, with a property for side, and a method to calculate the area of the square, which is the same as the area of a rectangle with length and width equal to the side of the square
class Square(Rectangle):
    def __init__(self, s, n = "Square"):
        # Calls the __init__ method of the parent class to initialize the area and name properties, setting the length and width from rectangle to the value of side
        super().__init__(s, s, n)
        # Protected instance variable for side, with placeholder blank value so it can still be used without error of not being initialized
        self._side = s
        
    # Property for side that waits to see if .side is called, and if it is, returns the value of the side
    @property
    def side(self):
        return self._side

    # Setter for side, that also recalculates the area when called, and checks for valid input, setting the length and width from rectangle to the value of side
    @side.setter
    def side(self, value):
        if value >= 0:
            self._side = value
            self._length = value
            self._width = value
            # Calls to calc_area to recalculate the area of the square when the side is changed
            self.calc_area()

# The main function that will test all of the shapes and their classes
def main():
    # List of all shapes and their info
    shapes = [
        Circle(0, 0, 5, "Circle_1"),
        Circle(2, 3, 4, "Circle_2"),
        Rectangle(4, 6, "Rectangle_1"),
        Rectangle(2, 18, "Rectangle_2"),
        Square(101, "Square_1"),
        Square(3, "Square_2")
    ]
    
    # Prints the name and shape of all shapes
    print("--- Polymorphism check ---")
    for shape in shapes:
        print(f"{shape.name} Area = {shape.area:.2f}")

    print()
    print("--- Getter/setter check ")

    # Prints different shapes according to index of the for loop, that will display their information, and then display the information once more after it has been modified, in this case, doubled
    circle = shapes[0]
    print(f"{circle.name} Current: {circle.radius}, {circle.area:.2f}")
    circle.radius = circle.radius * 2
    print(f"{circle.name} Doubled: {circle.radius}, {circle.area:.2f}")

    rectangle = shapes[2]
    print(f"{rectangle.name} Current: {rectangle.length}, {rectangle.width} {rectangle.area:.2f}")
    rectangle.length = rectangle.length * 2
    rectangle.width = rectangle.width * 2
    print(f"{rectangle.name} Doubled: {rectangle.length}, {rectangle.width} {rectangle.area:.2f}")

    square = shapes[4]
    print(f"{square.name} Current: {square.side}, {square.area:.2f}")
    square.side = square.side * 2
    print(f"{square.name} Doubled: {square.side}, {square.area:.2f}")

# Runs main
if __name__ == "__main__":
    main()