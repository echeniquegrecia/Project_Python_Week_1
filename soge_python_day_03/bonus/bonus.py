#!/usr/bin/python3
#!/usr/bin/python3
import datetime

class Titan(object):

    def __init__(self, name, age, size_in_meters, speed, energy):
        self._name = name
        self._age = age
        self._size_in_meters = size_in_meters
        self._speed = speed
        self._energy = energy

    def getName(self):
        return self._name
    
    def getAge(self):
        return self._age

    def getSizeInMeters(self):
        return self._size_in_meters

    def getSpeed(self):
        return self._speed

    def getEnergy(self):
        return self._energy

    def setName(self, name):
        if type(name) is str:
            self._name = name
        else:
            print("Invalid parameter")
    
    def setAge(self,age):
        if type(age) is int:
            self._age = age
        else:
            print("Invalid parameter")

    def setSizeInMeters(self, size_meters):
        if type(size_meters) is float:
            self._size_meters = size_meters
        else:
            print("Invalid parameter")

    def setSpeed(self, speed):
        if type(speed) is float:
            self._speed = speed
        else:
            print("Invalid parameter")
    
    def setEnergy(self,energy):
        if type(energy) is int:
            self._energy = energy
        else:
            print("Invalid parameter")

class AmericanTitan(Titan):

    def __init__(self, name, age, size_in_meters, speed, family_name, transformation_date, energy):
        super().__init__(name, age, size_in_meters, speed, energy)

    def to_eat_titan(titan_object):
        if titan_object is 
