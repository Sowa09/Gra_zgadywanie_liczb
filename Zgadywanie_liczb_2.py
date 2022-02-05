def user_number():
    """User input random number"""
    user_input = ["too small", "too big", "you won"]
    while True:
        user_answer = input().lower()
        if user_answer in user_input:
            break
        print("Input is not in ['too small', 'too big', 'you won']")
    return user_answer


def guess_number():
    """Main function"""
    print("Imagine number between 0 and 1000")
    print("Press enter to continue")
    input()
    min = 0
    max = 1000
    user_answer = ""
    while user_answer != "you won":
        guess = int((max - min) / 2) + min
        print(f"Your number is {guess}")
        user_answer = user_number()
        if user_answer == "too big":
            max = guess
        elif user_answer == "too small":
            min = guess
    print("You guess")


if __name__ == '__main__':
    guess_number()
