import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

letters_dict = {row.letter:row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.



def generate_word():
    word = input("Give a word:").upper()
    letter_in_word = list(word)
    try:
        code_list = [letters_dict[letter] for letter in letter_in_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_word()
    else:
        print(code_list)

generate_word()