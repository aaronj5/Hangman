word = "coding"

allowed_errors = 8
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")

        else:
            print("_", end = " ")
    print("")
