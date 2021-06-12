import random
def evil_word(file):
    with open(file) as word_list:
        text = word_list.read().split()

    ### 4 letters word; randomly sample 40 words;
    four_letters_words = random.sample([word for word in text if len(word)==4],k=40)
    sample_4letters= ['fifo', 'Ivan', 'hire', 'undo', 'Addu', 'tuwi', 'snob', 'imbe', 'pean', 'list', 'stey', 'Jose', 'wear', 'mian', 'Esth', 'Cuba', 'esne', 'Luba', 'limp', 'penk', 'phon', 'axle', 'wren', 'emir', 'ipid', 'Teri', 'yali', 'Omar', 'slod', 'glor', 'rave', 'mess', 'daze', 'Bixa', 'felt', 'Sika', 'nais', 'sadr', 'iced', 'flak']
    small_sample= []
    output = ""

    input_letter_size= input("Please enter How many letters the word contain: ")
    if input_letter_size=="4":
        small_sample= ['fifo', 'Ivan', 'hire', 'undo', 'Addu', 'tuwi', 'snob']
        output= "_ _ _ _"
    print(output)

    total_tries = 0
    while total_tries < 8:
        ## game field
        input_letter= input(f"guess 1 letter at each time, you have {8-total_tries} times guesses left!")
        family_dic= {}
        guess_collection =[]
        family_key = ""

        for word in small_sample: 
            family_key = word
            for letter in word:
                if letter != input_letter:
                    family_key = family_key.replace(letter, "_")
            if family_key in family_dic:
                family_dic[family_key].append(word)
            else:
                family_dic[family_key]= [word]
                ##family key complete
        #     print(family_dic[family_key])
        # print(len(family_dic))
        #e.g., {'_i__': ['fifo', 'hire'], '____': ['Ivan', 'undo', 'Addu', 'snob']}


        small_sample = get_max_list(family_dic)
        print("max list = " + str(small_sample))
        total_tries = total_tries + 1
    print("Sorry, you lose!")
    try_again = input("Do you want to play again? yes -- to try again, no -- end the game. ")
    if try_again == "yes":
        evil_word(file)
    else: 
        print("Bye!")

#### family_dict
def get_max_list(family_dict):
    max_list = []
    # finally max subset
    for value in family_dict.values():
        if len(value) > len(max_list):
            max_list = value
    return max_list





























if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        evil_word(file)
    else:
        print(f"{file} does not exist!")
        exit(1)