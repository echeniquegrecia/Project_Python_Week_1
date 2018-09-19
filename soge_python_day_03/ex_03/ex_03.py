#!/usr/bin/python3

class Titan(object):

    def __init__(self):
        self._name = "toto"
        self._age = 10
        self._size_in_meters = 1.8
        self._speed = 30.5

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

    @staticmethod
    def destroy():
        print('“Deeesssttrroyyy !')