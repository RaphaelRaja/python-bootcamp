import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data)

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)

user_word = input("Enter a word:").upper()

phonetic_list = [nato_dict[word] for word in user_word]
print(phonetic_list)
