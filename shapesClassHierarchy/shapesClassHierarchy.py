#

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