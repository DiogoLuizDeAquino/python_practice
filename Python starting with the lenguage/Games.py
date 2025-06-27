import MiniGameForca
import MiniGameDivinationDefinitive

print('########################################')
print('***********Choose a Game!!*************')
print('########################################')

print('(1) Forca-Game (2) Divination-Game')

game = int(input("What game do you wanna play?: "))

if(game == 1):
    print("You chose the Forca-Gmme!")
    MiniGameForca.play()
elif(game == 2):
    print("You chose the Divination-Game!")
    MiniGameDivinationDefinitive.play()