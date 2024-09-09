print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`." ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to One Piece.")
print("Your mission is to find the treasure of the King of Pirate, Gol D. Roger.")
road_1 = input("You're at a Jaya Island. Where do you want to go?\n"
               "    Type 'up' or 'sail'\n").lower()

if road_1 == "up":
    road_2 = input("You've come to Skypiea. There is Shandora the Gold City in the middle of the island.\n"
                   "    Type 'wait' to wait for friends to venture or type 'go' to go alone.\n").lower()
    if road_2 == "go":
        print("You get attacked by Enel. Game Over.")
    else:
        road_3 = input("You arrive at Shandora unharmed. There are 4 guardians waiting to battle you.\n"
                       "Ohm, Satori, Shura and Gedatsu. Which guardian do you want to battle?\n").lower()
        if road_3 == "ohm":
            print("You got caught in Ordeal of Iron. Game over.")
        elif road_3 == "satori":
            road_4 = input("You defeated Satori! Enel is waiting for you. Do you wish to defeat Enel?\n"
                           "    Type 'yes' to encounter Enel or type 'no' to return to Skypiea.\n").lower()
            if road_4 == "yes":
                print("You defeated Enel! You get your first Poneglyph, found the mystery of Shandora "
                      "and get closer to One Piece!")
            else:
                print("You are returning to Skypiea. Game over.")
        elif road_3 == "shura":
            print("You got caught in Ordeal of String. Game over.")
        elif road_3 == "gedatsu":
            print("You ended up befriending Gedatsu and forget to find One Piece. Game over.")
        else:
            print("You choose a wrong guardian, Saint Garcia Saturn come to punishes you. Game over.")
else:
    print("Sea beasts crush your ship and crews. Game over.")
