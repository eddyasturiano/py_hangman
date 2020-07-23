import random

winning_word = random.choice(["python", "java", "kotlin", "javascript"])
winning_letters = set(winning_word)

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
        guessed_letters = set() 
        lives = 8 
        # Main code
        while lives > 0:
            print()
            print(clue) # Each loop print the progress and get the letter 
            guess = input("Input a letter: ")
            if len(guess) == 1: 
                if guess.islower(): 
                    if guess in winning_letters:
                        if guess in guessed_letters:
                            print("You already typed this letter")
                        else:
                            guessed_letters.add(guess)
                            clue = ""  # Generate the progress string
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
