print('#######################################')
print('Welcome to this basic divination GAME!!')
print ('######################################')

secret_number = 73
attempt = ""

while (attempt != secret_number):
    attempt_str = input("Find the secret number, take your best shot: ")

    print("The number what you chose is: ", attempt_str)
    attempt = int(attempt_str)

    if(secret_number == attempt):
        print("Well done, you found the secret number!!!")
    else:
        if(attempt > secret_number):
            print("Wrong! Your number is too high than the secret number!!")
        elif(attempt < secret_number):
            print("Wrong! Your number is too low than the secret number!!")

print("End of the game :)")

