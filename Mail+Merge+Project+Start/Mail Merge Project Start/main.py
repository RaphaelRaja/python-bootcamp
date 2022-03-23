# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# defining name list
name_list = []

with open("./Input/Names/invited_names.txt") as name_file:
    for name in name_file:
        name_list.append(name)

# Opening the file
source_file_list = []
with open("./Input/Letters/starting_letter.txt") as source_file:
    # print(source_file.readlines())
    for lines in source_file:
        print("lines: " + lines)
        source_file_list.append(lines)

# creating and writing new files
for name in name_list:
    new_file_path = "./Output/ReadyToSend/" + name + ".txt"
    with open(new_file_path, 'w') as destination_file:
        for line in source_file_list:
            print(line)
            if line.rfind("Dear") == 0:
                temp = line.replace("[name]", name.strip())
                print("After edit:" + temp)
                destination_file.write(temp)
            else:
                destination_file.write(line)
