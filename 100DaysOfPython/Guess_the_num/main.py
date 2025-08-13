import random
from art import logo
easy_lives = 10
hard_lives = 5


def set_difficulty():
    difficulty = input("Choose a difficulty, 'easy' or 'hard' ").lower()
    if difficulty == "easy":
        return easy_lives
    else:
        return hard_lives

def guess(user_guess, number):
    if user_guess == number:
        return user_guess
    elif user_guess > number:
        print("Too high")
        return user_guess
    elif user_guess < number:
        print("Too low")
        return user_guess

def game():
    number = random.randint(1, 100)
    lives = set_difficulty()
    print(f"You start with {lives} lives.")

    while lives > 0:
        user_guess = int(input("Guess the number: "))
        check = guess(user_guess, number)
        if check == number:
            print("You WIN!!!")
            break
        else:
            lives -= 1
            print(f"You have {lives} lives left")
    if lives == 0:
        print(f"You lose! the number was: {number}")
is_running = True

while is_running:
    print(logo)
    more = input("Do you want to play guess the number? 'y' or 'n' ").lower()
    if more == "y":
        game()
    else:
        print("Buh bye")
        is_running = False






