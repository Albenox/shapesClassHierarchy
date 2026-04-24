#

# Abstract base class that holds the basic shape properties and methods
from abc import ABC, abstractmethod

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
