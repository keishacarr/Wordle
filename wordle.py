import random

with open ('dictionary.txt') as fin:
    data = fin.read().splitlines()

with open ('letters.txt') as fin:
    letters = [s.strip() for s in fin.read().split(',')]

word = random.choice(data)
#word = data[0]

guess = ""
guess_count = 1
wrong_letters = set()
right_letters = set()
unused = set(letters)

while guess != word:
    guess = input("Enter your guess: ").lower()
    
    # check if guess is a dictionary word
    while guess not in data:
        print ("\t", guess.upper(), "is not a dictionary word.")
        guess = input("Enter your guess: ")
    
    if guess == word:
        print("You guessed", word.upper(), "in", guess_count, "guesses.")

    else:
        print("guess #", guess_count)
        # compare guess and word, letter by letter
        for i in range (0,5):
            unused.discard(guess[i])
            if guess[i] == word[i]: #right char, right position
                print (guess[i].upper(), end=' ')
                right_letters.add(guess[i])
            else:
                print ("_", end=' ')
                if word.find(guess[i]) != -1: #right char, wrong position
                    right_letters.add(guess[i])
                else: #not in word
                    wrong_letters.add(guess[i])
            
        print("\n\tright:", right_letters)
        print("\tunused letters:", unused)
        print("\twrong:", wrong_letters)
    
        if guess_count == 6:
            print("\nAfter 6 guesses, you were unable to guess", word.upper())
            guess = word
        
        guess_count += 1