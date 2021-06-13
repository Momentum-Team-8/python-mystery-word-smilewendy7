### Notes:
# how to handle case sensitive?
# tell the user the word is used before!
import random
def evil_word(file):
    with open(file) as word_list:
        text = word_list.read().split()

    ### 4 letters word; randomly sample 40 words;
    # four_letters_words = random.sample([word for word in text if len(word)==4],k=40)
    sample_4letters= ['fifo', 'Ivan', 'hire', 'undo', 'Addu', 'tuwi', 'snob', 'imbe', 'pean', 'list', 'stey', 'Jose', 'wear', 'mian', 'Esth', 'Cuba', 'esne', 'Luba', 'limp', 'penk', 'phon', 'axle', 'wren', 'emir', 'ipid', 'Teri', 'yali', 'Omar', 'slod', 'glor', 'rave', 'mess', 'daze', 'Bixa', 'felt', 'Sika', 'nais', 'sadr', 'iced', 'flak']
    # small_sample= []
    output = ""
    correct_guess_collection =[]
    uess_collection =[]

    input_letter_size= input("Please enter How many letters the word contain: ")
    if input_letter_size=="4":
        small_sample= ['fifo', 'kiko', 'ffio', 'kkoi', 'tito', 'ttoi', 'poxy', 'piop']
        # small_sample=random.sample([word for word in text if len(word)==4],k=60)
        output= "_ _ _ _"
    print(output)

    total_tries = 0
    while total_tries < 10:
        ## game field
        input_letter= input(f"guess 1 letter at each time, you have {10-total_tries} times guesses left!")
        uess_collection.append(input_letter)
        print(f"Used letters: {sorted(uess_collection)}")

        family_dic= {}
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

        small_sample = get_max_list(family_dic)

        ##### *********  show the reduced list ********************
        print("max list = " + str(small_sample))
        ##### *********  show the reduced list ********************
        
        # print(input_letter)

        #make correct guess collection for the final word: 
        for word in small_sample:
            if len(small_sample)==1 and input_letter in small_sample[0]:
                output = small_sample[0]
                correct_guess_collection.append(input_letter)
            for letter in word:
                if letter not in correct_guess_collection:
                    output = output.replace(letter, "_")

        ##### hint shows on the playground:
        if input_letter in correct_guess_collection: 
            print(f"Yes, there are {input_letter} in the word!!")
        else:
            print(f"Sorry, there are no {input_letter} 's.")

        if output == small_sample[0]:
            print("Congradulations! You win!!!")
            try_again = input("Do you want to play again? yes -- to try again, no -- end the game. ")
            if try_again == "yes":
                evil_word(file)
            else: 
                print("Bye!")
                exit()
        print(output)
        # print(len(correct_guess_collection))
        
        total_tries = total_tries + 1

        ###******** chance to win *************
        chance_to_win = 100-len(small_sample)/40*100+2.5/4*len(correct_guess_collection)
        print(f" *** you got {chance_to_win} % chance to win the word!! ***")
        ###******** chance to win *************
        print(family_dic)
    
    print(f"Sorry, you lose!, the word is {random.choice(small_sample)}")
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