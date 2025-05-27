# 1-The program takes a command line argument, this argument is the name of a text file.
# the program reads all the text and split them and calculate
# the 20 most used words in the file  and then
# write them to a file called popular_words.txt
import sys
from collections import Counter
import re

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py filename.txt")
        return

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read().lower()
            words = re.findall(r'\b\w+\b', text)  # Extract words only

            word_counts = Counter(words)
            top_20 = word_counts.most_common(20)

            with open("popular_words.txt", "w", encoding='utf-8') as out_file:
                for word, count in top_20:
                    out_file.write(f"{word}: {count}\n")

            print("Top 20 words written to 'popular_words.txt'")

    except FileNotFoundError:
        print(f"File '{input_file}' not found.")

if __name__ == "__main__":
    main()

# 2-Given two points represented as x1, y1, x2, y2, r the
# (float)return (float) distance between
# them considering the following distance equation.

def equation(x1, y1, x2, y2):
    x_side = (math.pow(x2- x1 ,2))
    y_side = (math.pow(y2- y1 ,2))

    d = math.sqrt(x_side + y_side)
    return d

# 3-Create a Vehicle class without any variables and methods
class Vehicle:
    pass

# 4-Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

# 5-Write a Python program to reverse a string word by word
def reverse_string_words(s):
    return ' '.join(s.split()[::-1])

# 6-Write a Python class which has two methods get_String and
# print_String. get_String accepts a string from the user
# and print_String prints the string in upper case
class StringHandler:
    def __init__(self):
        self.string = ""

    def get_String(self):
        self.string = input("Enter a string: ")

    def print_String(self):
        print(self.string.upper())


# 7-Write a Python class named Circle
# constructed by a radius and two methods
# which will compute the area and the perimeter of a circle
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
