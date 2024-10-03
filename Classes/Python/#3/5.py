# 5. Optional Lab:
# You can actually make a simple command line game. You could put together everything
# you've learned so far about Python. The game goes like this:
# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#  Close: You've guessed a correct number but in the wrong position
#  Match: You've guessed a correct number in the correct position
#  Nope: You haven't guess any of the numbers correctly
# 4. Based on these clues you will guess again until you break the code with a
#  perfect match!
# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:
# Try to figure out what this code is doing and how it might be useful to you
import random


# digits = list(range(10))
# random.shuffle(digits)
# print(digits[:3])
# Think about how you will compare the input to the random number, what format should they be in? Maybe some sort of sequence?


def close(guessArray, digits):
    return sum(1 for g in guessArray if g in digits) - match(guessArray, digits)


def match(guessArray, digits):
    return sum(1 for g, d in zip(guessArray, digits) if g == d)


def nope(guessArray, digits):
    return len(guessArray) - match(guessArray, digits) - close(guessArray, digits)


def guessNumber(digits):
    guess = input("What is your guess? \n")
    if not guess.isdigit() or len(guess) != 3:
        print("Please enter 3-digit number")
        return guessNumber(digits)
    guessArray = [int(char) for char in guess]
    print(f"Your guess:{guess}")
    if digits == guessArray:
        print("Congratulation! You guessed the number!")
        return
    matchAmount = match(guessArray, digits)
    closeAmount = close(guessArray, digits)
    nopeAmount = nope(guessArray, digits)

    print(f"Match:{matchAmount}\nClose:{closeAmount}\nNope:{nopeAmount}")
    guessNumber(digits)


def main():
    while True:
        digits = list(range(10))
        random.shuffle(digits)
        digits = digits[:3]
        # print(digits) #Uncomment for debug
        guessNumber(digits)
        choice = input("Do you want to play again?(Y/N)\n").strip().lower()
        if choice != "y":
            print("Thanks for playing!")
            break


main()
