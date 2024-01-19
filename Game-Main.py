import random

with open('hangman.txt', 'r') as f: #opens a file of specific words for the game to pick from (educational related)
    words = f.readlines()

word = random.choice(words).strip()

allowed_errors = 8 
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"Allowed Errors Left {allowed_errors}, Next Guess?:").lower().strip()

    
    if not guess.isalpha() or len(guess) != 1: #Verifies if input is a valid character, and blocks numbers
        print("Please enter a valid single letter.")
        continue

    
    if guess not in word.lower(): # Check if the guessed letter is not in the word
        allowed_errors -= 1
        if allowed_errors == 0:
            break

    done = all(letter.lower() in guesses for letter in word)

  
    if guess not in guesses:
        guesses.append(guess)

if done: #end game message, win or lose
    print(f"Congratulations, you have found the word: {word}!")
else:
    print(f"Game Over :( The word was: {word}!")
