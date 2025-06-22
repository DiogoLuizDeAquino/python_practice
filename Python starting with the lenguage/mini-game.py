print('#######################################')
print('Welcome to this basic divination GAME!!')
print ('######################################')

secret_number = 73
attempt = ""
chance = 5
attempt_str = input("Find the secret number. You have 5 chances! Press 'ENTER' to continue ")

while (chance > 0):
    chance_str = input("Take your best shot:")
  

    print("The number of chances you have: ", chance)
    attempt = int(chance_str)

    if(secret_number == attempt):
        print("Well done, you found the secret number!!!")
    else:
        if(attempt > secret_number):
            print("Wrong! Your number is too high than the secret number!!")
        elif(attempt < secret_number):
            print("Wrong! Your number is too low than the secret number!!")

    chance = chance -1
    if(chance <= 0):
            print("Your chances are DONE!!!")
        

print("End of the game :)")

