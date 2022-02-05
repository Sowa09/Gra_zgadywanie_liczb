import random


def player_number():
    """
    Get number from user
    :return:
    """
    while True:
        try:
            player_choice = int(input("Guess the number: "))
            break

        except ValueError:
            print("It's not a number!")
    return player_choice


def computer_guess():
    """
    Get number from user and compare with computer random choice.
    :return:
    """
    computer_choice = random.randint(1, 100)
    player_choice = player_number()
    while player_choice != computer_choice:
        if player_choice < computer_choice:
            print("To small")
        else:
            print("Too big")

        player_choice = player_number()
    print("You win")


if __name__ == '__main__':
    computer_guess()
