#Guess number between 1-20.

import random
times = 0
comp_number = 0
comp_number = random.randrange(1,21)

print("Guess a number between 1 - 20 : ")
guessed_number =int(input())

while guessed_number != comp_number:
    times+=1
    
    if guessed_number > comp_number:
        print(" Your number is too  big.")
        guessed_number = int(input("Please try again: "))


    if guessed_number < comp_number:
        print(" Your number is too  small.'")
        guessed_number = int(input("Please try again: "))

    if guessed_number == comp_number:
        print(" You guessed the exact number")
        break;
print (f"You needed {times} to win the game.")

