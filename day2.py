import os
import random


# 1-Given a list of numbers, create a function that returns a list where all similar adjacent
# elements have been reduced to a single element, so [1,2,3.3] returns [1,2,3]
# Note:
# You may create a new list or modify the passed in list.
def remove_adjacent_duplicates(lst):
    result = []
    for num in lst:
        if not result or result[-1] != num:
            result.append(num)
    return result


# 2-Consider dividing a string into two halves
# Case1:
# The length is even, the front and back halves are the same length.
# Case2:
# The length is odd, we’ll say that the extra char goes in the front half.
# E.g. ‘abced’, the front half is ‘abc’, the back half’de.
# Given 2 strings, a and b, return a string of the form:
# (a-front + b-front) + (a-back +b-back)

def split_and_merge(a, b):
    def split_string(s):
        mid = (len(s) + 1) // 2
        return s[:mid], s[mid:]

    a_front, a_back = split_string(a)
    b_front, b_back = split_string(b)

    return a_front + b_front + a_back + b_back

# 3- Write a Python function that takes a sequence of numbers and determines
# whether all the numbers are different from each other.
# E.X. [1,5,7,9] -> True
# [2,4,5,5,7,9] -> False

def all_unique(lst):
    return len(lst) == len(set(lst))


# 4- Given unordered list, sort it using algorithm bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


# 5- Guesses game
# ● Your game generates a random number and gives only 10 tries for the user to
# guess that number.
# ● Get a user input and compare it with the random number
# ● Display a hit message to the user in case the use number is smaller or bigger of
# the random number
# ● If the user type number is out of range(100), display a message that is not allowed
# and don’t count this as try.
# ● If user type a number that has been entered before, display a hint message and
# don’t count this as try
# ● In case the user entered a correct number within the 10 tries, display a
# congratulations message and let your application guess another random number
# with the remain number of tries
# ● If the user finishes all his tries, display a message to ask him if he wants to play
# again or not.


def guessing_game():
    max_attempts = 10
    attempts_left = max_attempts
    guessed_numbers = set()

    while attempts_left > 0:
        target_number = random.randint(1, 100)
        print(f"\nA new number has been generated! You have {attempts_left} attempts left.")

        while attempts_left > 0:
            try:
                guess = int(input("Enter a number between 1 and 100: "))

                if guess < 1 or guess > 100:
                    print("Out of range! Please enter a number between 1 and 100.")
                    continue

                if guess in guessed_numbers:
                    print("You've already guessed this number! Try a different one.")
                    continue

                guessed_numbers.add(guess)
                attempts_left -= 1

                if guess < target_number:
                    print("Too low! Try again.")
                elif guess > target_number:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You guessed the number {target_number} correctly!")
                    break

            except ValueError:
                print("Invalid input! Please enter a valid number.")

        if attempts_left == 0:
            print("\nYou've used all your attempts! Would you like to play again? (yes/no)")
            if input().lower() == "yes":
                attempts_left = max_attempts
                guessed_numbers.clear()
            else:
                print("Thanks for playing! Goodbye.")
                break

guessing_game()

# 6- Diagonal Difference on Hackerrank

def diagonalDifference(arr):
    prim = 0
    sec = 0
    length = len(arr[0])
    for count in range(length):
        prim += arr[count][count]
        sec += arr[count][(length - count - 1)]
    return abs(prim - sec)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
