import random
def mystery_word(file):
    with open(file) as word_list:
        text = word_list.read().split()
        print(text)

        ## level 1 words
        l1_words = [ word for word in text if len(word)>=6]
        l2_words = []

        input_level= input("Choose a level of difficulty")

        if input_level == "easy": 
            #select a random word
            selected_word = random.choice(l1_words)
            print(selected_word)
            print(f"this word has {len(selected_word)} letters")

            guess_input= input("Please guess 1 letter per round")
            output_word= ""
            i=0
            guess_collection = []
            while output_word != selected_word:
                output_word = selected_word
                i+=1
                if guess_input in selected_word:
                    guess_collection.append(guess_input)
                print(f" here is {guess_collection}")
                for letter in selected_word:
                    if letter not in guess_collection:
                        output_word = output_word.replace(letter, "_")
                        
                print(output_word)
                if output_word == selected_word:
                    print("you win!")
                    break
                if i==8:
                    print("Sorry, you lose!!")
                    break
                else:
                    guess_input= input(f"Please guess 1 letter per round, {8-i} times left to try!")
        

        























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