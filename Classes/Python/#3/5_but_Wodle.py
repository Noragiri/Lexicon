import random
import os


def clear_terminal():
    # Check if the operating system is Windows
    if os.name == "nt":
        os.system("cls")  # Command for Windows
    else:
        os.system("clear")  # Command for Unix-like systems (Linux, macOS)


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def drawWordle(guesses, digits):
    clear_terminal()
    print("=" * len(digits))
    lastGuess = guesses[len(guesses) - 1]
    row = ""
    for index, number in enumerate(lastGuess):
        if number == digits[index]:
            row = row + bcolors.OKGREEN + str(number) + bcolors.ENDC
        elif number in digits:
            row = row + bcolors.OKCYAN + str(number) + bcolors.ENDC
        else:
            row = row + bcolors.FAIL + str(number) + bcolors.ENDC
    guesses[len(guesses) - 1] = row

    for guess in guesses:
        print(guess)
    print("=" * len(digits))


def guessNumber(previousGuesses, digits):
    guess = input("What is your guess? \n")
    if not guess.isdigit() or len(guess) != len(digits):
        print(f"Please enter {len(digits)}-digit number")
        return guessNumber(digits)
    guessArray = [int(char) for char in guess]
    if digits == guessArray:
        print(
            f"{bcolors.OKGREEN}Congratulation! You guessed the number!{bcolors.ENDC}{bcolors.WARNING}\nIt took you {len(previousGuesses)+1} attempt(s){bcolors.ENDC}"
        )
        return
    previousGuesses.append(guessArray)
    drawWordle(previousGuesses, digits)
    guessNumber(previousGuesses, digits)


def selectDifficulty():
    difficultyInput = input("Select amount of digits to guess (up to 10)\n")
    try:
        if int(difficultyInput) > 0 and int(difficultyInput) <= 10:
            return int(difficultyInput)
        else:
            print("Amount must be between 1 and 10\n")
            selectDifficulty()
    except ValueError:
        print("Please input a number :)\n")
        selectDifficulty()


def main():
    while True:
        previousGuesses = []
        clear_terminal()
        diffculty = selectDifficulty()
        digits = list(range(10))
        random.shuffle(digits)
        digits = digits[:diffculty]
        # print(digits)  # Uncomment for debug
        guessNumber(previousGuesses, digits)
        choice = input("Do you want to play again?(Y/N)\n").strip().lower()
        if choice != "y" and choice != "yes":
            print("Thanks for playing!")
            break


main()
