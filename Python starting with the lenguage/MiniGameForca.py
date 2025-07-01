def play():
    print('#######################################')
    print('Welcome to this basic forca GAME!!')
    print ('######################################')

    secret_word = "banana"
    hanged = False
    guessed = False

    while not hanged and not guessed:
        guess = input("Type a letter: ")
        guess = guess.strip()

        index = 0
        for letter in secret_word:
            if (guess.upper == letter.upper()):
                print("You found the letter {} in the position {}".format(letter, index))
            index = index + 1
        print("Playing...")

print("End of the game")

if __name__ == "__main__":
    play()
