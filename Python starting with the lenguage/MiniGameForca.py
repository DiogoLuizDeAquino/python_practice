def play():
    print('#######################################')
    print('Welcome to this basic forca GAME!!')
    print ('######################################')

    secret_word = "banana"
    list_right_letters = ["", "", "", "", "", ""]

    hanged = False
    guessed = False
    count_errors = 0

    while not hanged and not guessed:
        guess = input("Type a letter: ")
        guess = guess.strip()

        if guess in secret_word:
            index = 0
            for letter in secret_word:
                if (guess.upper() == letter.upper()):
                    list_right_letters[index] = letter
                index = index + 1
        else:
            count_errors = count_errors + 1

        print("Playing...")
        print(list_right_letters)

print("End of the game")

if __name__ == "__main__":
    play()
