import random
def mystery_word(file):
    with open(file) as word_list:
        text = word_list.read().split()

        ## level 1 words
        easy = [ word for word in text if len(word)>=4 and len(word)<=6 ] 
        normal = [ word for word in text if len(word)>=6 and len(word)<=8] 
        hard = [ word for word in text if len(word)>8] 
       
        input_level= input("Welcome to the game! Please choose a level of difficulty: easy, normal, or hard")
        
        if input_level == "easy": 
            #select a random word
            selected_word = random.choice(easy)
        elif input_level == "normal": 
            selected_word = random.choice(normal)
        else: 
            selected_word = random.choice(hard)
        print(f"this word has {len(selected_word)} letters")

        # guess_input= input("Please guess 1 letter per round")
        guess_collection = []
        output_word= ""
        i=0
        correct_guess_collection = []
        while output_word != selected_word:
            while i<8:
                guess_input= input(f"Please guess 1 letter per round, you have {8-i} times left to try!")
                if guess_input not in guess_collection:
                    guess_collection.append(guess_input)
                    output_word = selected_word
                    i+=1
                else:
                    print(f" you guessed {guess_input} before, please try other letters!")

                if guess_input in selected_word:
                    correct_guess_collection.append(guess_input)
                # print(f" here is {correct_guess_collection}")
                for letter in selected_word:
                    if letter not in correct_guess_collection:
                        output_word = output_word.replace(letter, "_")   
                print(output_word)
                
            if i==8:
                print(f"Sorry, you lose!! The word is {selected_word}")
                try_again = input("Do you want to play again? yes -- to try again, no -- end the game. ")
                if try_again == "yes":
                    mystery_word(file)
                else: 
                    print("Bye!")
                    exit()
     
        if output_word == selected_word:
            print("you win!")
            try_again = input("Do you want to play again? yes -- to try again, no -- end the game. ")
            if try_again == "yes":
                mystery_word(file)
            else: 
                print("Bye!")

        























if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        mystery_word(file)
    else:
        print(f"{file} does not exist!")
        exit(1)