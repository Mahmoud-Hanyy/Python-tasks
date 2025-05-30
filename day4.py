#1-Define a class attribute "color" with a default value white. I.e.,
# Every Vehicle should be white.

class Vehicle:
    color = "white"  # Class attribute with default value

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

# 2- Create a Bus child class that inherits from the Vehicle class.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        maintenance_charge = base_fare * 0.10
        total_fare = base_fare + maintenance_charge
        return total_fare

# 3-Determine if School_bus is also an instance of the Vehicle class

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

# Check if School_bus is an instance of Vehicle class
print("Is School_bus an instance of Vehicle?", isinstance(School_bus, Vehicle))


# 4-Define a class named Rectangle which can be constructed by a length and width. The
# Rectangle class has a method which can compute the area.
# Hints: Use def methodName(self) to define a method.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# 5- Define a class which has at least two methods: getString:
# to get a string from console input printString:
# to print the string in upper case.

class StringHandler:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())



# 6-Define a class Person and its two child classes: Male and Female. All classes have a
# method "getGender" which can print "Male" for Male class and "Female" for Female
# class.

class Person:
    def __init__(self, name):
        self.name = name

    def getGender(self):
        print("Unknown gender")


class Male(Person):
    def getGender(self):
        print("Male")


class Female(Person):
    def getGender(self):
        print("Female")

# 7- Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
# These brackets must be close in the correct order, for example "()" and "()[]{}" are valid
# but "[)", "({[)]" and "{{{" are invalid

class ParenthesesValidator:
    def __init__(self):
        self.opening = {'(', '[', '{'}
        self.closing = {')', ']', '}'}
        self.pairs = {'(': ')', '[': ']', '{': '}'}

    def isValid(self, s):
        stack = []
        for char in s:
            if char in self.opening:
                stack.append(char)

            elif char in self.closing:

                if not stack:
                    return False

                last_opening = stack.pop()

                if self.pairs[last_opening] != char:
                    return False

        return len(stack) == 0

# 8- Hackerrank Class 2 - Find the Torsional Angle
import math
class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)
    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z
    def cross(self, no):
        return Points(self.y * no.z - self.z * no.y, self.z * no.x - self.x * no.z, self.x * no.y - self.y * no.x)
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))