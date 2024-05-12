#Guess number between 1-20.

import random

def handle_input(comp_number):
    user_input = input()
    if user_input=='x':
        exit()
    if user_input=='n':
        return True, 0
    if user_input=='s':
        print("Cheating! Number to guess is:", comp_number)
        return handle_input(comp_number)
    return False, int(user_input)
    

def main_game():
    times = 0
    comp_number = 0
    comp_number = random.randrange(1,21)

    print("Guess a number between 1-20:")
    to_break, guessed_number = handle_input(comp_number)
    times+=1

    while (guessed_number != comp_number) and (not to_break):
        times+=1
        
        if guessed_number > comp_number:
            print("Your number is too high.")
            print("Please try again: ")
            to_break, guessed_number = handle_input(comp_number)


        if guessed_number < comp_number:
            print("Your number is too low.")
            print("Please try again:")
            to_break, guessed_number = handle_input(comp_number)

        if guessed_number == comp_number:
            print("You guessed the exact number")
            break;
    print (f"You needed {times} to win the game.")

def main():
        main_game()
        to_play_again = input("Would you like to play again? (y/n)")
        while(to_play_again=='y'):
            main_game()
            to_play_again = input("Would you like to play again? (y/n)")

if __name__ == "__main__":
    main() 