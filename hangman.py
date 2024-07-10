HANGMAN_PHOTOS = {1: """    x-------x """, 2: """    x-------x
    |
    |
    |
    |
    | """, 3: """    x-------x
    |       |
    |       0
    |
    |
    | """, 4: """    x-------x
    |       |
    |       0
    |       |
    |
    | """, 5: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    | """, 6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    | """ , 7: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    | """}
    
    
def show_hidden_word(secret_word, old_letters_guessed):
    """construct a string of _ and letters to show the progress of the player
    :letter_guessed: string
    :old_letters_guessed: list of singl letter strings
    :return: rez
    :rtype: string
	"""
    
    rez = ""
    for l in secret_word:
        if l in old_letters_guessed:
            rez += l
            rez += " "
        else:
            rez += "_ "
    rez = rez[:-1]
    
    return rez  

def check_win(secret_word, old_letters_guessed):
    """Finds if letters guessed are in secret word.
    :secret_word: string
    :old_letters_guessed: list of singl letter strings
    :return: True or False 
    :rtype: Boolean
	"""


    for l in secret_word:
        if l not in old_letters_guessed:
            return False
        
    return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Finds if letters guessed is legal
    :letter_guessed: string
    :old_letters_guessed: list of singl letter strings
    :return: True or False and add letter_guessed to old_letters_guessed 
    :rtype: Boolean
	"""
    
    arrow = " -> "
    old_letters_guessed.sort()
    if len(letter_guessed) != 1:
       print("X")
       print(arrow.join(old_letters_guessed))
       return False
    
    low_list = letter_guessed.lower()
   
    if low_list in old_letters_guessed:
        print("X")
        print(arrow.join(old_letters_guessed))
        return False
        
    if low_list.isalpha() == False:
        print("X")
        print(arrow.join(old_letters_guessed))
        return False
    
    else:
        old_letters_guessed += low_list[0]
        return True

def choose_word(file_path, index):
    """pulling out the secret word from file
    :file_path: string, file location
    :index: int
    :return: a word according to the index 
    :rtype: string
	"""
    fl = open(file_path, "r")
    word_l = []
    for line in fl:
        for word in line.split():
            word_l += [word]
    
    word_num = len(word_l)        
    
    while word_num < index:
        index = index - word_num
    
    uniq_w = []
    cunt = 0
    
    for w in word_l:
        if w not in uniq_w:
            cunt +=1
            uniq_w += [w]
        
    
    return  word_l[index-1] 


error = 1   



HANGMAN_ASCII_ART = "Welcome to the game Hangman"
MAX_TRIES = 6
print(HANGMAN_ASCII_ART)
print("""   _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/ """)


print(MAX_TRIES)    
 
linck_file = input("please enter sicret word file:") 
word_file = open(linck_file, 'r')

secret_word_list = []
for line in word_file:
    for word in line.split():
        if word not in secret_word_list:
            secret_word_list.append(word)

word_file.close()

list_len = len(secret_word_list)

secret_insex = input("please enter the secret word number:")

while secret_insex >= list_len or secret_insex is not int:
    print("the secret number must be a NUMCER between 0 and ", (list_len - 1))
    secret_insex = input("please enter the secret word number:")

secret_word = choose_word(linck_file, secret_insex)

errors = 1
word_len = len(secret_word)
old_letters_guessed = []
win = False
print(HANGMAN_PHOTOS[1])

while errors < 7 and  win == False :
    show_hidden_word(secret_word, old_letters_guessed)
    

    guess_l = input("guess a letter:")
    chek = try_update_letter_guessed(guess_l, old_letters_guessed)
    while chek == False:
        guess_l = input("guess a letter:")

    old_letters_guessed += guess_l

    if guess_l in secret_word:
        print ("V")
        
    else:
        errors += 1    
        print(HANGMAN_PHOTOS[errors])

    win = check_win(secret_word, old_letters_guessed) 

if win == True:
    print("Well done, You found the secret word!")
    print(secret_word)

else:
    print("You didn't succeeded this time, Try again?")
    print("the secret wors was ", secret_word )