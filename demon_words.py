# next steps:
# 1) fix case sensitive 2) add reminder of type 1 letter at a time

## game rules:
# 4 levels: 3,4,5,6 letters
# 15 times to try

### game secrect: 
# ** only 1 words left or the max family has the same pattern, I will always pick the first word in the list as the fianl word.
import random
def evil_word(file):
    with open(file) as word_list:
        text = word_list.read().split()

    ### randomly sample 40 words from each word list;
    three_letters_words = random.sample([word for word in text if len(word)==3],k=40)
    four_letters_words = random.sample([word for word in text if len(word)==4],k=40)
    five_letters_words = random.sample([word for word in text if len(word)==5],k=40)
    six_letters_words = random.sample([word for word in text if len(word)==6],k=40)

    output = ""
    correct_guess_collection =[]
    guess_collection =[]

    input_letter_size= input("Please enter How many letters the word contain: Please enter 3 or 4 or 5 or 6 ")
    if input_letter_size=="3":
        small_sample=three_letters_words
        output= "_ _ _ "
        print(output)

    if input_letter_size=="4":
        small_sample=four_letters_words
        output= "_ _ _ _"
        print(output)
    
    if input_letter_size=="5":
        small_sample=five_letters_words
        output= "_ _ _ _ _"
        print(output)

    if input_letter_size=="6":
        small_sample=five_letters_words
        output= "_ _ _ _ _ _"
        print(output)

    total_tries = 0
    while total_tries < 15:
        ## game field
        input_letter= input(f"guess 1 letter at each time, you have {15-total_tries} times guesses left!")
        if input_letter not in guess_collection:
            guess_collection.append(input_letter)
            total_tries = total_tries + 1

        else: 
            print(f"Hi, you guessed {input_letter} before, please try other letters!")
        print(f"Used letters: {sorted(guess_collection)}")

        family_dic= {}
        family_key = ""
        ### make the dic of word family
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
        # print(f"max list = {small_sample}")
        ##### *********  show the reduced list ********************

        #make correct guess collection for the final word: 
        for word in small_sample :
            if input_letter in small_sample[0]:
                output = small_sample[0]
                correct_guess_collection.append(input_letter)
            for letter in small_sample[0]:
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

        ###******** chance to win *************
        chance_to_win = 100-len(small_sample)/40*100 + 1/len(output)* len(correct_guess_collection)
        #  2.5/len(output)
        print(f" *** you are {chance_to_win} % close to win the word!! ***")
        ###******** chance to win *************
    
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