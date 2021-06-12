import random
def evil_word(file):
    with open(file) as word_list:
        text = word_list.read().split()

    ### 4 letters word; randomly sample 40 words;
    four_letters_words = random.sample([word for word in text if len(word)==4],k=40)
    sample_4letters= ['fifo', 'Ivan', 'hire', 'undo', 'Addu', 'tuwi', 'snob', 'imbe', 'pean', 'list', 'stey', 'Jose', 'wear', 'mian', 'Esth', 'Cuba', 'esne', 'Luba', 'limp', 'penk', 'phon', 'axle', 'wren', 'emir', 'ipid', 'Teri', 'yali', 'Omar', 'slod', 'glor', 'rave', 'mess', 'daze', 'Bixa', 'felt', 'Sika', 'nais', 'sadr', 'iced', 'flak']
    small_sample= ['fifo', 'Ivan', 'hire', 'undo', 'Addu', 'tuwi', 'snob']
    print(small_sample)

    ## game field
    input_letter= input("make your first guess")
    words_dic= {}
    family_dic= {}
    guess_collection =[]
    family_key= ""

    ## words_dic: show each chr
    for word in small_sample: 
       words_dic[word]=[chr for chr in word]
       # e.g., fifo': ['f', 'i', 'f', 'o'], 'Ivan': ['I', 'v', 'a', 'n']
    print(words_dic)

    for li in words_dic:
        # li: key, value: words_dic[li][1]
        family_key= li
        for letter in li:
            if letter != input_letter:
                family_key= family_key.replace(letter, "_")
    # family_dic[family_key]=words_dic[word]
        print(family_key)
        