import random

wrong = 0
decks = {"deck_a": ["some", "thing", "ehe"],
         "deck_b": ["project", "very", "sad"]
         }

word_list = None


already_guessed = []
print("All decks : deck_a , deck_b")
deck_name = input("Please type your deck name to choose the deck : ")

word_list = decks[deck_name]

the_word = random.choice(word_list)
the_word = the_word.upper()
print("The word had been chosen")


word_display: str = "_"

for i in range(1, len(f'{the_word}')):
    word_display += " _"

print(word_display)

# Game loop
while True:
    guess = input("Guess a letter: ")
    guess = guess.upper()
    if guess == "" or guess == " ":
        continue

    if guess not in already_guessed:
        already_guessed.append(guess)

        if guess in the_word:  # If the guess is correct
            for letter in already_guessed:
                for i in range(0, len(the_word)):
                    if str(letter) == str(the_word[i]):
                        strlst = list(word_display)
                        strlst[2 * i] = letter
                        word_display = ''.join(strlst)
            if "_" not in word_display:
                print("YOU DID IT!")
                print(word_display)
                break
        else:
            wrong += 1
            print(f"Wrong {wrong} time(s)")
            if wrong >= 7:
                print("GAME OVER!")
                break
        print(word_display)
    else:
        print('That letter have been guessed!')
