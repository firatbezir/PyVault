#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_txt = letter.read()    # read() returns string whereas readlines() returns list object


names = open("./Input/Names/invited_names.txt")
names_list = names.readlines()

PLACEHOLDER = "[name]"

for new_name in names_list:
    new_name = new_name.strip("\n")
    personalized_letter = letter_txt.replace(PLACEHOLDER, new_name)

    with open(f"./Output/ReadyToSend/letter_for_{new_name}.docx", "w") as file:
        file.write(personalized_letter)


#
# import os, glob
# folder_path = "./Output/ReadyToSend"
# txt_files = glob.glob(os.path.join(folder_path, "*.txt"))
#
# for file in txt_files:
#     os.remove(file)
#     print(f"Deleted: {file}")
