import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
# 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
code = {value.letter: value.code for (index, value) in df.iterrows()}

# 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("What is your name? ").upper()
code_name = [code[letter] for letter in name]
print(code_name)
print(code["A"])
