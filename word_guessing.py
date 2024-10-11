import random
name = input("What is your name? ")
choice = input(f"Welcome, {name}, to the Word Guessing Game! Do you want to choose the words? Please choose Yes or No: ").lower()
words = []

if choice == "yes":
    print("Alright, enter the words you want to use in the game.")
    print("If you want to exit the game, type 'q'.")
    while True:
        choose = input("Choose a word: ").lower()
        if choose == "q":
            break
        words.append(choose)

if choice == "no":
    print("Alright, you will play with the pre-established words.")
    words = ['rainbow', 'computer', 'science', 'programming',
             'python', 'mathematics', 'player', 'condition',
             'reverse', 'water', 'board', 'geeks']
    
print(words)

word = random.choice(words)
print(word)
print("Guess the characters")
guesses = {}
turns = 12

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    
    print()
    
    if failed == 0:
        print("Congratulations! You win!")
        print(f"The word was {word}")
        break

    guess = input("Guess a character: ").lower()
    
    if guess in word:
        if guess in guesses:
            print("You have already chosen this letter, please try another.")
        else:
            guesses[guess] = 1
    else:
        turns -= 1
        print(f"Incorrect guess, please try again. You have {turns} turns left.")

if turns == 0:
    print(f"Sorry, you've run out of turns. The word was {word}.")
