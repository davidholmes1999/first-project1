#David Holmes
#3/9/17
#Number Simulator


#Print Statements

print("\nWeclome to the number simulator game! You will be seeing how many guesses it takes for you to guess my number!\n")
print("\nFirst let me think of a number between 1 and 100\n")
print("\nHmmmmmm...\n")

import random

#Defining Variables

player=int(input("\nI got it! Guess wisely, I can be a trickster! Now plesase type in a number between 1-100.\n"))

computer=random.randint(1,100)

#If Statements

x= 1
while player != computer:

    if player>computer:
        print("\nGuess lower...")

    elif player<computer:
        print("\nGuess higher...")

    x= x+1

    player= int(input("\nGuess again please...\n"))

#Outro Statement

print("\nYou guessed the number right! It took you", x, "attempts to guess it! Good job!\n")

#Input Statement

input("\n\nPress enter to continue")
