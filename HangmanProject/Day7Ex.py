#Ex1 Random world

import random

#Step 1 
word_list = ["aardvark", "baboon", "camel"]

#T#ODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# random_number = random.randint(0,2)
# chosen_word = word_list[random_number]
chosen_word = random.choice(word_list)
#T#ODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess=input("Guess a letter ").lower()
#T#ODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")

#Ex2 Replacing Blanks

#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#T#ODO-1: - Create an empty List called display.
display=[]
for position in chosen_word:
    display += "_"
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

guess = input("Guess a letter: ").lower()

#T#ODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for pos in range(0, len(chosen_word)): # a in aadwark=> a==a=>display[0] 
    if chosen_word[pos]== guess:    
        display[pos]=guess
    #    display.append(f"{guess}")
    # else:
        # display.append("_")

#T#ODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)