import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
print(logo)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

lives = 6

game_over = False
display = []
display += list(placeholder)
guessed = []
print(stages[-1])
#replace with equivalent index in placeholder
while game_over != True:
    guess = input("Guess a letter: ").lower()
    if guess in guessed:
        print(f" You have already guessed {guess}")
        continue
    else:
        guessed.append(guess)

    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"Incorrect, you have {lives} lives left")
    print(stages[lives])
    print("".join(display))
    if "_" not in display:
        print("You Win")
        game_over = True
    elif lives == 0:
        print(f"The word was {chosen_word} you lose")
        game_over = True