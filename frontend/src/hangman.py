import random
import time

# Starts timer
t0 = time.time()

abc = []

build_word = []

wrong_count = []

# Opens words.txt and gets random word from there
secret_word = random.choice(open("words.txt","r").readline().split())

# Prints the word user is guessing + guessed letters
def letters():
    print("  Word:     " + " ".join(build_word))
    print("\n" + "  Letters:  " + " ".join(abc) + "\n")

# Starts the game and makes the secret word with "_"
def start_game(secret_word):
    for i in secret_word:
        build_word.append("_")
    user_input()

# Ask and takes users letters, input
def user_input():
    title()
    hangman(len(wrong_count))
    print(" ")
    letters()
    letter = input("\n" + "  Enter a letter: ").lower()
    good_letter(letter)

# Tells is the guessed letter correct or have user already guessed it
def good_letter(a):
    if a in abc:
        print("\n" + "  !!! Already guessed that !!!")
        user_input()
    elif a.isalpha() and len(a) == 1:
        abc.append(a)
        letter_test(a)
    else:
        print("\n" + "  !!! Try again !!!")
        user_input()

# Tests does the users letters match to the secret word
def letter_test(b):
    if b in secret_word:
        find_location(secret_word, b)
    else:
        wrong_letter(b)

# Tries to find letters correct place in a secret word
def find_location(string, letter):
    location = []
    last_index = -1
    while True:
        try:
            last_index = string.index(letter, last_index + 1)
        except ValueError:
            break
        else:
            location.append(last_index)
    add_letter(letter, location)

# Adds letter to the secret word
def add_letter(letter, location_list):
    for position in location_list:
        build_word[position] = letter
    word_test(secret_word)

# Tests is the word same as the secret word
def word_test(compare):
    if build_word == list(compare):
        winner()
    else:
        user_input()

# Counts wrong guesses
def wrong_letter(d):
    if len(wrong_count) < 8:
        wrong_count.append(d)
        user_input()
    else:
        loser()

# Stops the timer, asks users name and saves the time and name in a text file. Saves top-3 best times per word
def save_high_score():
    t1 = time.time()
    total = int(t1 - t0)
    print()
    print("  It took: ", total, "seconds")
    
    save_name = input("  Enter your name: ")

    with open('high_score.txt', 'r') as r:
        word_group = {}

        for line in r.readlines():
            word, score, name = line.split(',')
            name = name.strip()
            if word in word_group:
                word_group[word].append((int(score), name))
            else:
                word_group[word] = [(int(score), name)]
        try:
            group = word_group[secret_word]
            values = [groups[0] for groups in word_group[word]]
            if len(group) < 3:
                group.append((total, save_name))
            elif total <= max(values):
                highest = max(group)
                group.remove(highest)
                group.append((total, save_name))
        except (UnboundLocalError, KeyError):
            word_group[secret_word] = [(int(total), save_name)]

        with open('high_score.txt', 'w') as file:
            for word, data in word_group.items():
                for d in data:
                    score = d[0]; save_name = d[1]
                    file.write(word + "," + str(score) + "," + save_name + "\n")

# Prints the high score board from the text file
def print_high_scores():
    print("\n" + "  --- TOP-3 HIGH SCORES ---" + "\n")
    with open('high_score.txt', 'r') as r:
        words = {}
        for line in r.readlines():
            word, score, name = line.split(',')
            name = name.strip()
            if word in words:
                words[word].append(name + ": " + score)
            else:
                words[word] = [name + ": " + score]

        for x in words:
            words[x].sort(key = lambda x: int(x.split(':')[1].strip()))
            print("'" + x + "':")
            for y in words[x]:
                print(y + " seconds")
            print("\n")

def loser():
    title()
    game_over()
    letters()


def winner():
    title()
    congratulations()
    letters()
    save_high_score()
    print_high_scores()

def title():
    print()
    print("  ,--.  ,--.  ,---.  ,--.  ,--. ,----.   ,--.   ,--.  ,---.  ,--.  ,--. ") 
    print("  |  '--'  | /  O  \ |  ,'.|  |'  .-./   |   `.'   | /  O  \ |  ,'.|  | ")  
    print("  |  .--.  ||  .-.  ||  |' '  ||  | .---.|  |'.'|  ||  .-.  ||  |' '  | ")  
    print("  |  |  |  ||  | |  ||  | `   |'  '--'  ||  |   |  ||  | |  ||  | `   | ")  
    print("  `--'  `--'`--' `--'`--'  `--' `------' `--'   `--'`--' `--'`--'  `--' ") 

def hangman(count):
    print()
    if count == 0:
        print("  Guesses left:", 9 - len(wrong_count))
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print("  ____________")
        print("  |          |____")
        print("  |______________|")
    elif count == 1:
        print("  Guesses left:", 9 - len(wrong_count))
        print()
        print()
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |___________")
        print("  |          |____")
        print("  |______________|")
    elif count == 2:
        print("  Guesses left:", 9 - len(wrong_count))
        print()
        print("  ___________")
        print("  |/")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |___________")
        print("  |          |____")
        print("  |______________|")
    elif count == 3:
        print("  Guesses left:", 9 - len(wrong_count))
        print()
        print("  ___________")
        print("  |/        |")
        print("  |         |")
        print("  |         |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |___________")
        print("  |          |____")
        print("  |______________|")
    elif count == 4:
        print("  Guesses left:", 9 - len(wrong_count))
        print()
        print("  ___________")
        print("  |/        |")
        print("  |         |")
        print("  |         |")
        print("  |         O")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |___________")
        print("  |          |____")
        print("  |______________|")
    elif count == 5:
        print("  Guesses left:", 9 - len(wrong_count))
        print()
        print("  ___________")
        print("  |/        |")
        print("  |         |")
        print("  |         |")
        print("  |         O")
        print("  |         |")
        print("  |         |")
        print("  |")
        print("  |")
        print("  |___________")
        print("  |          |____")
        print("  |______________|")
    elif count == 6:
        print("  Guesses left:", 9 - len(wrong_count))
        print()
        print("  ___________")
        print("  |/        |")
        print("  |         |")
        print("  |         |")
        print("  |         O")
        print("  |        /|")
        print("  |         |")
        print("  |")
        print("  |")
        print("  |___________")
        print("  |          |____")
        print("  |______________|")
    elif count == 7:
        print("  Guesses left:", 9 - len(wrong_count))
        print()
        print("  ___________")
        print("  |/        |")
        print("  |         |")
        print("  |         |")
        print("  |         O")
        print("  |        /|\ ")
        print("  |         |")
        print("  |")
        print("  |")
        print("  |___________")
        print("  |          |____")
        print("  |______________|")
    elif count == 8:
        print("  Guesses left:", 9 - len(wrong_count))
        print()
        print("  ___________")
        print("  |/        |")
        print("  |         |")
        print("  |         |")
        print("  |         O")
        print("  |        /|\ ")
        print("  |         |")
        print("  |        /")
        print("  |")
        print("  |___________")
        print("  |          |____")
        print("  |______________|")

def game_over():
    print()
    print("  ___________")
    print("  |/        |")
    print("  |         |")
    print("  |         |")
    print("  |         O")
    print("  |        /|\ ")
    print("  |         |")
    print("  |        / \ ")
    print("  |")
    print("  |___________")
    print("  |          |____")
    print("  |______________|")
    print()
    print("  !!! GAME OVER !!!")
    print()

def congratulations():
    print()
    print("                                   .''.")
    print("         .''.             *''*    :_\/_: ")
    print("        :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'")
    print("    .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-")
    print("   :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'")
    print("   : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *")
    print("    '..'  ':::'   * /\ * |'|  .'/.\'.  '._____")
    print("        *        __*..* |  |     :      |.   |' .---'|")
    print("         _*   .-'   '-. |  |     .--'|  ||   | _|    |")
    print("      .-'|  _.|  |    ||   '-__  |   |  |    ||      |")
    print("      |' | |.    |    ||       | |   |  |    ||      |")
    print("   ___|  '-'     '    ''       '-'   '-.'    '`      |____")
    print("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("  Fireworks over city - Cleveland (c) Joan Stark")
    print()
    print("  !!! YOU GUESSED THE WORD !!!")
    print()

# Starts the game using secret word which is from text file
start_game(secret_word)