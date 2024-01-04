import random

with open('hangman.txt', 'r') as f: #randoms guessing words from the provided list in hangman.txt
    words = f.readlines()

word = random.choice(words)[:-1]  #Word for player to guess

allowed_errors = 8 
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses: #Ignores case sensitivity
            print(letter, end=" ")

        else:
            print("_", end = " ")
    print("")


    guess = input(f"Allowed Errors Left {allowed_errors}, Next Guess?:") #Notifys player how many guess they have
    guesses.append(guess.lower())
    if guess.lower () not in word.lower():
        allowed_errors -= 1 #subtract amount of guesses left
        if allowed_errors == 0: #Amount of guesses remain
            break

    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done: #End of game prompts
    print(f"Congratulations, you have found the word, {word} ! ")
else:
    print(f"Gave Over :( The word was {word} ! ")
