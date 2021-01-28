import random
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def game():
    print("Welcome to Blackjack")
    def card():
        return random.choice(cards)

    def calculate_winner(p_current_score, c_current_score):
        if p_current_score > 21 and c_current_score > 21:
            return "No winner"
        elif p_current_score > 21:
            return "You lose"
        elif p_current_score < c_current_score and c_current_score < 21:
            return  "You lose"
        elif p_current_score > c_current_score and p_current_score < 21:
            return  "You win"
        elif p_current_score < c_current_score and c_current_score > 21:
            return  "You win"
        elif p_current_score > c_current_score and c_current_score < 21:
            return  "You lose"
        elif p_current_score == c_current_score:
            return "No winner"

    c_card1 = card()
    p_card1 = card()
    p_card2 = card()

    player_hand = [p_card1, p_card2]
    p_current_score = p_card1 + p_card2

    print("First round")
    print(f"Your cards: {player_hand}, final score: {p_current_score}")
    print(f"Computer's first card: {c_card1}")
    second_round = input("Type 'y' to get another card, type 'n' to pass ")

    c_card2 = card()
    c_current_score = c_card1 + c_card2
    computer_hand = [c_card1, c_card2]
    if c_current_score < 17:
        c_card3 = card()    
        c_current_score += c_card3
        computer_hand.append(c_card3)

    if second_round=="n":    
        print(f"\nSecond round\nComputer's final hand: {computer_hand}, final score: {c_current_score}")
        print(calculate_winner(p_current_score, c_current_score))       
    else:
        p_card3 = card()
        player_hand.append(p_card3)
        p_current_score += p_card3 
        print(f"\nYour cards: {player_hand}, final score: {p_current_score}")
        print(f"Second round\n computer's final hand: {computer_hand}, final score: {c_current_score}")
    
        print(calculate_winner(p_current_score, c_current_score))        
    
    if input("\nDo you want to play again? 'y' or 'n' ") == "y":
        clear()
        game()
game()