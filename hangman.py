import random

# Randomly choose a word and separate its letters
winning_word = random.choice(["python", "java", "kotlin", "javascript"])
winning_letters = set(winning_word)

# A string with only dashes the same length as the winning word to be displayed the first time the main code loops
clue = ""
i = 0
while i < len(winning_word):
    clue += "-"
    i += 1


print("H A N G M A N\n")

# Player menu
while True:
    play_or_quit = input('Type "play" to play the game, "exit" to quit:')
    if play_or_quit == "play":
        guessed_letters = set() # Initialize the set of letters the player has guessed
        lives = 8 # Initialize the total number of lives the player has
        # Main code
        while lives > 0:
            print()
            print(clue) # Each loop print the progress and get the letter the player inputs
            guess = input("Input a letter: ")
            if len(guess) == 1: # Check if the user prints exactly one letter
                if guess.islower(): # Check if the user prints and English lowercase letter
                    if guess in winning_letters:
                        if guess in guessed_letters:
                            print("You already typed this letter")
                        else:
                            guessed_letters.add(guess)
                            clue = ""  # Generate a string which is the player's progress
                            for letter in winning_word:
                                if letter in guessed_letters:
                                    clue += letter
                                else:
                                    clue += "-"
                            if "-" not in clue:  # Win condition
                                print("You guessed the word!")
                                print("You survived!")
                                break
                    else:
                        if guess in guessed_letters:
                            print("You already typed this letter")
                        else:
                            print("No such letter in the word")
                            lives -= 1
                            guessed_letters.add(guess)
                else:
                    print("It is not an ASCII lowercase letter")
            else:
                print("You should input a single letter")
        else:
            print("You are hanged!")
    else:
        break