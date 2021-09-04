print(''' 
_                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|

''')
print("Welcome to the treasure island \n ")
direction=input("Choose your direction left or right \n ").lower()
if direction=="left":
    skill=input("Do you want to wait or swim \n ").lower()
    if skill=="wait":
        door=input("Choose your favourite door: red, green or yellow \n ").lower()
        if door=="green":
            print("Congratulations!! you have won the treasure")
        elif door=="red":
            print("You are busted")
        elif door=="yellow":
            print("Monsters killed you ")
        else:
            print("You have choosen the wrong color! Please try again ")
    else:
        print("You are drowned")
else:
    print("Game over!")
