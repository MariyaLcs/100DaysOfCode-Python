import pandas


#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {value.letter: value.code for (key, value) in data.iterrows()}
print(new_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Write your word ").upper()
letters = [new_dict[letter] for letter in word]
print(letters)