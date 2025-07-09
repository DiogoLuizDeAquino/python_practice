def play():
    print('#######################################')
    print('Welcome to this basic forca GAME!!')
    print ('######################################')

    secret_word = "banana".upper()
    list_right_letters = ["", "", "", "", "", ""]

    hanged = False
    guessed = False
    count_errors = 0

    print(list_right_letters)

    while not hanged and not guessed:
        guess = input("Type a letter: ")
        guess = guess.strip().upper()

        if guess in secret_word:
            index = 0
            for letter in secret_word:
                if (guess == letter):
                    list_right_letters[index] = letter
                index += 1
        else:
            count_errors += 1

        hanged = count_errors == 6
        print(list_right_letters)

    print("End of the game")

if __name__ == "__main__":
    play()

#Preciso continuar na lógica da forca, voltando a editar o game