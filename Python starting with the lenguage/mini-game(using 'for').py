import random

print('#######################################')
print('Welcome to this basic divination GAME!!')
print('######################################')

secret_number = random.randrange(1,101) #101 to avoid null/zero numbers
total_chances = 5
print("Difficulty levels: (1) Fácil,(2) Médio ,(3) Difícil")
input("choose the difficulty level: ")

input("Find the secret number. You have {} chances! Press 'ENTER' to continue ".format(total_chances))

for current_chance in range(1, total_chances + 1):
    print("Number of chances left:", total_chances - current_chance + 1)
    guess_str = input("Take your best shot: ")
    guess = int(guess_str)
   

    if secret_number == guess:
        print("Well done, you found the secret number!!!")
        break
    else:
        if guess > secret_number:
            print("Wrong! Your number is too high!")
        elif guess < secret_number:
            print("Wrong! Your number is too low!")

    if current_chance == total_chances:
        print("Your chances are DONE!!!")

print("End of the game :)")
