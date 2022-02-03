# https://www.programiz.com/python-programming/property

class Celcius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

# We now upgrade and introduce setters and getters

class Celcius2:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32
    
    def get_temperature(self):
        return self._temperature # The underscore indicates private variable

    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

class Celcius3:
    def __init__(self, temperature = 0):
        self.temperature = temperature  # this line has changed back

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32 # this line has changed back
    
    def get_temperature(self):
        print("Getting value...")
        return self._temperature # The underscore indicates private variable

    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # Creating temperature object
    temperature = property(get_temperature, set_temperature)
    
class Celcius4:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")        
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below 273 is not possible.")
        self._temperature = value


if __name__ == '__main__':
    
   # Create a new object 
   human = Celcius()

   # Set the temperature
   human.temperature = 37

   # Get the temperature attribute
   print(human.temperature)

   # Get the to_fahrenheit method
   print(human.to_fahrenheit())

   print("""\nWhenever we assign or retrieve an attribute like temperature as shown
above, Python searches it in the object's built-in __dict__ dictionary
attribute: {}. Therefore man.temperature internally becomes 
man.__dict__['temperature']""".format(human.__dict__)) 

   # Let's now use the upgraded class when in reality we would have just 
   # upgraded Celcius, PLEASE bear this in mind

   # Create a new object 
   human = Celcius2(37)

   # Get the temperature attribute using getter
   print("\n{}".format(human.get_temperature()))

   # Get the to_fahrenheit method, which calls the get_temperature() method itself
   print(human.to_fahrenheit())

   print("""\nIt's important to note at this point that there's no such thing as a 
private variable in python.""")

   print("""\nWe now have the problem that all the places in the code base where
all the programs that have implemented the original Celcius Class, where the code base
has a getter 'obj.temperature' -> 'obj.get_temperature()' and setter
'obj.temperature = val' -> obj.set_temperature(val).""")

   print("""\nThis is where the '@property' comes in so we don't have to go back
through the code  and find all of the old setters and getters and remake them.
The '@property' decorator makes the new setters and getters backward compatible.""")

   # Create a new object 
   human = Celcius3(37)                 # new way to set
   human.temperature = 50               # old way to set
   print(human.get_temperature())       # new way to get
   print(human.temperature)             # old way to get 


   
   print("""Thanks to the print statements in Celcius3 we can see the Getters and Setters 
are now being called rather than the dunder dictionary attribute, despite them, 
not being explicitly called in the __init__.\nAny line that contains 
self.temperature = temperature now calls set_temperature() and any line that calls
self.temperature now calls get_temperature(). Therefore we now have a backwards
compatible attributeAny line that contains 
self.temperature = temperature now calls set_temperature() and any line that calls
self.temperature now calls get_temperature(). Therefore we now have a backwards
compatible attributes.""")
    
# property objects have three methods, getter(), setter(), deleter()
# so the line below 
# temperature = property(get_temperature, set_temperature)
# can be written as
 
# MAKE EMPTY PROPERTY
# temperature = property()

# ASSIGN fget
# temperature = temperature.gettter(get_temperature)

# ASSIGN sget
# temperature = temperature.setter(set_temperature)

   print("""\nFinally in Celcius4 we can use the @property method to clear the class 
further method.""") 
    
   human = Celcius4(37)
   print(human.temperature)
   print(human.to_fahrenheit())
   coldest_thing = Celcius(300) 
