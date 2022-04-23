import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data)

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)


def generate_phonetic():
    user_word = input("Enter a word:").upper()
    try:
        phonetic_list = [nato_dict[word] for word in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_list)


generate_phonetic()
