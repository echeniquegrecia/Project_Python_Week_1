#!/usr/bin/python3
import datetime

class Titan(object):

    def __init__(self, name, age, size_in_meters, speed):
        self._name = name
        self._age = age
        self._size_in_meters = size_in_meters
        self._speed = speed

    def getName(self):
        return self._name
    
    def getAge(self):
        return self._age

    def getSizeInMeters(self):
        return self._size_in_meters

    def getSpeed(self):
        return self._speed

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

class RoyalTitan(Titan):

    def __init__(self, name, age, size_in_meters, speed, family_name, transformation_date):
        super().__init__(name, age, size_in_meters, speed)
        self.__family_name = family_name
        self.__transformation_date = transformation_date

    def getFamilyName(self):
        return self.__family_name

    def getTransformationDate(self):
        return self.__transformation_date    

    def setFamilyName(self, family_name):
        if type(family_name) is str:
            self.__family_name = family_name
        else:
            print("Invalid parameter")
    
    def setTransformationDate(self, transformation_date):
        if type(transformation_date) is datetime.date:
            self.__transformation_date = transformation_date
        else:
            print("Invalid parameter")


class DeviantTitan(Titan):

    def __init__(self, name, age, size_in_meters, speed, deviance_index, errors):
        super().__init__(name, age, size_in_meters, speed)
        self.__deviance_index = deviance_index
        self.__errors = errors

    def getDevianceIndex(self):
        return self.__deviance_index

    def getErrors(self):
        return self.__errors    

    def setDevianceIndex(self, deviance_index):
        if type(deviance_index) is int:
            if deviance_index in range(1,11):
                self.__deviance_index = deviance_index
            else:
                print("Invalid parameter")
        else:
            print("Invalid parameter")
    
    def setErrors(self, errors):
        if type(errors) is int:
            self.__errors = errors
        else:
            print("Invalid parameter")