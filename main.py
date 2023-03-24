import random


def get_the_number():
    """Get number from user.

    Try until user gives a proper number.

    :rtype: int
    :return: given number as int
    """
    while True:
        try:
            guess = int(input("Guess the number:"))
            return guess
        except ValueError:
            print("This is not a number!")


def guess_the_number():
    """This function checks whether we guessed the number correctly"""
    number = random.randint(1, 100)
    guessed_number = get_the_number()
    while guessed_number != number:
        if guessed_number < number:
            print("Too small!")
        else:
            print("Too big!")
        guessed_number = get_the_number()
    print("You win!")



if __name__ == '__main__':
    guess_the_number()
