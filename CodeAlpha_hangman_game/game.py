import random

# List of predefined words
words = ["python", "java", "apple", "computer", "coding"]

# Choose a random word
word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")

while attempts > 0:
    display_word = ""
    
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    
    print("\nWord:", display_word)
    print("Attempts left:", attempts)

    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word correctly.")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct guess!")
    else:
        guessed_letters.append(guess)
        attempts -= 1
        print("Wrong guess!")

if attempts == 0:
    print("\n❌ Game Over! The word was:", word)
