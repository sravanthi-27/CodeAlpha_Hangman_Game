import random
print("Hello! Great to have you here! Let's play Hangman")
print("Please enter your name to begin the adventure")
name=input("My name is:")
def get_random_word():
    words = ["python", "java", "swift", "programming", "hangman", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return display

def play_hangman():
    word = get_random_word()
    guessed_letters = set()
    attempts_remaining = 6
    guessed_word = False

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while not guessed_word and attempts_remaining > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! {display_word(word, guessed_letters)}")
        else:
            guessed_letters.add(guess)
            attempts_remaining -= 1
            print(f"Wrong guess. You have {attempts_remaining} attempts remaining.")
            print(display_word(word, guessed_letters))

        guessed_word = all(letter in guessed_letters for letter in word)

    if guessed_word:
        print(f"Congratulations! You've guessed the word '{word}'.")
        print(f"You won! '{name}'Your guessing skills are top-notch")
    else:
        print(f"Sorry, you've run out of attempts. The word was '{word}'.")
        print(f"Better luck next time '{name}'! Appreciate your game spirit!")
if __name__ == "__main__":
    play_hangman()