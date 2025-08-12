import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(your_cards):
    current_score = sum(your_cards)
    while current_score > 21 and 11 in your_cards:
        your_cards.remove(11)
        your_cards.append(1)
        current_score = sum(your_cards)
    return current_score

def player_turn(your_cards, dealer_cards):
    is_playing = True
    current_score = calculate_score(your_cards)
    print(f"Your cards: {your_cards}, Current score: {current_score}")
    print(f"Dealer card: {dealer_cards[0]}")
    if current_score == 21:
        print("BlackJack!")
        is_playing = False

    while is_playing:


        hit_or_stand = input("Would you like to 'hit' or 'stand?' ").lower()

        if hit_or_stand == "hit":
            new_card = random.choice(cards)
            your_cards.append(new_card)
            new_score = calculate_score(your_cards)
            print(f"Your cards: {your_cards}, Current score: {new_score}")
            if new_score > 21:
                #print(f"You draw: {new_card} current score is: {new_score}")
                is_playing = False
            elif new_score == 21:
                print("21!")
                is_playing = False
            else:
                continue
        elif hit_or_stand == "stand":
            is_playing = False
    final_score = calculate_score(your_cards)
    print(f"Your score: {final_score} and hand: {your_cards}")
    return final_score

def dealer_turn(dealer_cards):
    dealer_score = calculate_score(dealer_cards)
    while dealer_score < 17:
        new_card = random.choice(cards)
        dealer_cards.append(new_card)
        dealer_score = calculate_score(dealer_cards)
    print(f"Dealer hand: {dealer_cards} final score: {dealer_score}")
    return dealer_score

def compare(player_score, dealer_score):
    if player_score > 21:
        print("BUST!!!")
    elif dealer_score > 21:
        print("DEALER BUST!! you win!")
    elif player_score == dealer_score:
        print("Draw!")
    elif player_score > dealer_score:
        print("You WIN!!!")
    else:
        print("You LOSE!!!")

def play_game():
    your_cards = [random.choice(cards), random.choice(cards)]
    dealer_cards = [random.choice(cards), random.choice(cards)]
    player_score = player_turn(your_cards, dealer_cards)
    dealer_score = dealer_turn(dealer_cards)
    compare(player_score, dealer_score)

print(art.logo)

running = True

while running:

    play = input("Would you like to play blackjack? 'y' or 'n' ").lower()
    print("\n" * 20)
    print(art.logo)
    if play == "y":
        play_game()
    else:
        running = False
