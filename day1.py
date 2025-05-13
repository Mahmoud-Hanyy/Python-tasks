import math
# Write a Python program which accepts the user's first and last name and print them in
# reverse order with a space between them.

print('Enter Your First Name: ')
first_name = input()
print('Enter Your First Name: ')
last_name = input()
print(last_name + ' ' + first_name)

# Write a Python program that accepts an integer (n) and computes the value of
#n+nn+nnn. Sample value of n is 5 , Expected Result : 615

number= str(input("Enter a number"))
print(int(number) + int(number+number)+int(number+number+number))

# Write a Python program to print the following here document.
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example

print('a string that you "don\'t" have to escape\nThis\nis a ....... multi-line\nheredoc string --------> example')

# Write a Python program to get the volume of a sphere with radius 6.

radius = 6
volume = 4 / 3 * math.pi * (math.pow(radius, 3))
print(volume)

# Write a Python program that will accept the base and height of a triangle and compute
# the area.

print('Enter the base: ')
base = int(input())
print('Enter the height: ')
height = int(input())
area =  1/2 * base * height
print(area)

# Write a Python program to construct the following pattern, using a nested for loop.
# Search about method
# end=””
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

n = 5
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print('')

for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')


# Write a Python program that accepts a word from the user and reverse it

print('Enter a word: ')
reversed_word = ""
word = input()
for i in reversed(word):
    reversed_word += i + ''
print(reversed_word)

# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

for i in range(7):
    if i % 3 !=0:
        print(i)

# Write a Python program to get the Fibonacci series between 0 to 50
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

a = 0
b = 1
next = b
count = 1

while count <= 50:
    print(next, end=" ")
    count += 1
    a, b = b, next
    next = a + b
print()

# Write a Python program that accepts a string and
# calculate the number of digits and letters.

print('Enter a string: ')
string = input()
length = string.__len__()
print(length)