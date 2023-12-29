import random

print("Welcome to Hangman")
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)

# Stages
stage = [
    ''' 
    +---+
    |   |
        |
        |
        |
        |
    =========
    ''', # stage 0
    '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    ''', # stage 1
    '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    ''', # stage 2
    '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    ''', # stage 3
    '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========
    ''', # stage 4
    '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========
    ''', # stage 5
    '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========
    ''' # stage 6
]



# Step 1
word_list = word_list = [
'abruptly',
'absurd',
'abyss',
'affix',
'askew',
'avenue',
'awkward',
'axiom',
'azure',
'bagpipes',
'bandwagon',
'banjo',
'bayou',
'beekeeper',
'bikini',
'blitz',
'blizzard',
'boggle',
'bookworm',
'boxcar',
'boxful',
'buckaroo',
'buffalo',
'buffoon',
'buxom',
'buzzard',
'buzzing',
'buzzwords',
'caliph',
'cobweb',
'cockiness',
'croquet',
'crypt',
'curacao',
'cycle',
'daiquiri',
'dirndl',
'disavow',
'dizzying',
'duplex',
'dwarves',
'embezzle',
'equip',
'espionage',
'euouae',
'exodus',
'faking',
'fishhook',
'fixable',
'fjord',
'flapjack',
'flopping',
'fluffiness',
'flyby',
'foxglove',
'frazzled',
'frizzled',
'fuchsia',
'funny',
'gabby',
'galaxy',
'galvanize',
'gazebo',
'giaour',
'gizmo',
'glowworm',
'glyph',
'gnarly',
'gnostic',
'gossip',
'grogginess',
'haiku',
'haphazard',
'hyphen',
'iatrogenic',
'icebox',
'injury',
'ivory',
'ivy',
'jackpot',
'jaundice',
'jawbreaker',
'jaywalk',
'jazziest',
'jazzy',
'jelly',
'jigsaw',
'jinx',
'jiujitsu',
'jockey',
'jogging',
'joking',
'jovial',
'joyful',
'juicy',
'jukebox',
'jumbo',
'kayak',
'kazoo',
'keyhole',
'khaki',
'kilobyte',
'kiosk',
'kitsch',
'kiwifruit',
'klutz',
'knapsack',
'larynx',
'lengths',
'lucky',
'luxury',
'lymph',
'marquis',
'matrix',
'megahertz',
'microwave',
'mnemonic',
'mystify',
'naphtha',
'nightclub',
'nowadays',
'numbskull',
'nymph',
'onyx',
'ovary',
'oxidize',
'oxygen',
'pajama',
'peekaboo',
'phlegm',
'pixel',
'pizazz',
'pneumonia',
'polka',
'pshaw',
'psyche',
'puppy',
'puzzling',
'quartz',
'queue',
'quips',
'quixotic',
'quiz',
'quizzes',
'quorum',
'razzmatazz',
'rhubarb',
'rhythm',
'rickshaw',
'schnapps',
'scratch',
'shiv',
'snazzy',
'sphinx',
'spritz',
'squawk',
'staff',
'strength',
'strengths',
'stretch',
'stronghold',
'stymied',
'subway',
'swivel',
'syndrome',
'thriftless',
'thumbscrew',
'topaz',
'transcript',
'transgress',
'transplant',
'triphthong',
'twelfth',
'twelfths',
'unknown',
'unworthy',
'unzip',
'uptown',
'vaporize',
'vixen',
'vodka',
'voodoo',
'vortex',
'voyeurism',
'walkway',
'waltz',
'wave',
'wavy',
'waxy',
'wellspring',
'wheezy',
'whiskey',
'whizzing',
'whomever',
'wimpy',
'witchcraft',
'wizard',
'woozy',
'wristwatch',
'wyvern',
'xylophone',
'yachtsman',
'yippee',
'yoked',
'youthful',
'yummy',
'zephyr',
'zigzag',
'zigzagging',
'zilch',
'zipper',
'zodiac',
'zombie',
]

# Randomly choose a word from the word_list
chosen_word = random.choice(word_list)
print(f"Btw, the secret word is: {chosen_word} ")

# Ask the user to guess a letter and convert it to lowercase (input already in the while loop below)


# Deconstruct the chosen word into a list of characters.
deconstructed_chosen_word = list(chosen_word)

# Initialize the board with underscores.
l = len(chosen_word)
#you can use display instead of board if you want
board = ["_"] * l
#print(f"The current board: {board}")

# Display the current state of the board.
#print(' '.join(board))

# Step 2


lives_left = 6

end_of_game = False

while not end_of_game:
    if "_" not in board:
        end_of_game = True
        print("You won!!!!!")
        break

    guess = input("Please make a guess of a letter you think may be inside the word! : \n").lower()

# Update the board based on the new guess.
    for position_on_board in range(l):
        # Display the updated state of the board.

        if guess == deconstructed_chosen_word[position_on_board]:
            board[position_on_board] = guess
    print(' '.join(board))
    if guess in deconstructed_chosen_word:
        print(f"Nice work! You guessed a correct letter! You chose '{guess}'")
    else:
        lives_left -= 1
        print(f"Sorry, but '{guess}' was not in this index place. 1 Life Lost! You have {lives_left} lives left.\n")
        print(f"{stage[lives_left]}")
        if lives_left == 0:
            print("You did not guess in time. Sorry, you lose! Try again!")
            break
else:
    print("You did not guess in time. Sorry, you lose! Try again!")

# Display the updated state of the board.
print(' '.join(board))

#User_Wins
