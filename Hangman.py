import random

#List of words
words = ["python", "java", "kotlin", "javascript", "hangman", "programming", "developer", "algorithm"]

#Randomly choose a word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")


while wrong_guesses < max_guesses:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("\nWord: " + display_word.strip())
    print("Wrong guesses left: " + str(max_guesses - wrong_guesses))
    
    guess = input("Enter a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    
    guessed_letters.append(guess)
    
    if guess not in word:
        wrong_guesses += 1
        print("Wrong guess!")
    
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word: " + word)
        break