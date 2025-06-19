print('#######################################')
print('Welcome to this basic divination GAME!!')
print ('######################################')

secret_number = 73
attempt_str = input("Find the secret number, take your best shot: ")

print("The number what you chose: ", attempt_str)
attempt = int(attempt_str)

if(secret_number == attempt):
    print("Well done, you found the secret number!!!")
else:
    print("You lose !!!")

print("End of the game :)")

