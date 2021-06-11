import random
def mystery_word(file):
    with open(file) as word_list:
        text = word_list.read().split()
        print(text)

        ## level 1 words
        l1_words = [ word for word in text if len(word)>=4 and len(word)<=6]

        input_level= input("Choose a level of difficulty")

        if input_level == "easy": 
            #select a random word
            selected_word = random.choice(l1_words)
            print(selected_word)
            print(f"this word has {len(selected_word)} letters")

            guess_input= input("Please guess 1 letter per round")

            list_selected_word = [char for char in selected_word]
            # print(list_selected_word)
            output_word= []
            i=0
            while output_word != list_selected_word:
                i+=1
                for letter in selected_word:
                    if letter == guess_input and i==1:
                        output_word.append(letter)
                    elif i==1:
                        output_word.append("_")
                    elif letter == guess_input:
                        j=(selected_word.index(letter))
                        output_word[j] = letter
                    else:
                        output_word
                print(output_word)
                if i==7:
                    print("Sorry, you lose!!")
                else:
                    guess_input= input("Please guess 1 letter per round")
                

            if output_word == list_selected_word:
                print("you win!")
            
            
        

        























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