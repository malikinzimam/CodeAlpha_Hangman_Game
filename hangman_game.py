import random

# Possible words list
word_list = ["python", "hangman", "developer", "programming", "challenge", "computer"]

# Select a random word
word = random.choice(word_list)
word_display = ["_"] * len(word)  # Underscores for hidden letters
attempts = 6  # Maximum incorrect guesses
guessed_letters = set()

print("Welcome to Hangman!")
print(" ".join(word_display))

while attempts > 0 and "_" in word_display:
    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter!")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.add(guess)

    if guess in word:
        print("Good guess!")
        for i in enumerate(word):
            if i == guess:
                word_display[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1
        print(f"Attempts left: {attempts}")

    print(" ".join(word_display))

# Game result
if "_" not in word_display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
