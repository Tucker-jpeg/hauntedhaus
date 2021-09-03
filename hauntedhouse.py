print('''
..                                            ,           ^'^  _
..                                            )               (_) ^'^
.        _/\_                    .---------. ((        ^'^
.        (('>                    )`'`'`'`'`( ||                 ^'^
    _    /^|                    /`'`'`'`'`'`\||           ^'^
    =>--/__|m---               /`'`'`'`'`'`'`\|
.        ^^           ,,,,,,, /`'`'`'`'`'`'`'`\      ,
.                    .-------.`|`````````````|`  .   )
                    / .^. .^. \|  ,^^, ,^^,  |  / \ ((
...                /  |_| |_|  \  |__| |__|  | /,-,\||
        _         /_____________\ |")| |  |  |/ |_| \|
...    (")         |  __   __  |  '==' '=='  /_______\     _
..    (' ')        | /  \ /  \ |   _______   |,^, ,^,|    (")
...    \  \        | |--| |--| |  ((--.--))  ||_| |_||   (' ')
.    _  ^^^ _      | |__| |("| |  ||  |  ||  |,-, ,-,|   /  /
^^^,' ',  ,' ',    |           |  ||  |  ||  ||_| |_||   ^^^
.,,|RIP|,.|RIP|,.,,'==========='==''=='==''=='=======',,....,,,,.,
''')


print("Welcome to the Haunted House.")
print("Your mision is to save trick-or-treaters lost in the house.\n")

choice1 = input('You are in front of the house, which way do you want to enter? Type "front door" or "window" and hit Enter \n')
if choice1.lower() == "window":
    choice2 = input('You snuck in through a window. You come to the foyer and can take the staircase upstairs or down to the basement. Type "basement" or "upstairs" and hit Enter to proceed \n')
    if choice2.lower() == "upstairs":
        choice3 = input("You go upstairs and are in a hallway with 3 doors to enter: 1 red, 1 green, 1 blue. Which color door do you choose? \n")
        if choice3.lower() == "red":
            print("The room is full of poisonous snakes! Game over.")
        elif choice3.lower() == "green":
            print("You found the lost trick-or-treaters and lead them out of the haunted house to safety. You win!")
        elif choice3.lower() == "blue":
            print("You ended up in a warewolf's room. It eats you! Game over.")
        else:
            print("This door doesn't exist... Game over.")
    else:
        print("You encountered a witch who cast a spell turning you into a rat! Game Over.")
else:
    print("You fell into a spike pit as you entered the house! Game Over.")




