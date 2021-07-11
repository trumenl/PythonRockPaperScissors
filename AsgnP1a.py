from random import randint


# Get user input for each match
def getmatchinput():
    t = ["0", "1", "2"]
    computer = t[randint(0, 2)]

    return computer, input("Enter 0(fire), 1(grass) or 2(water):")


# Calculate and display result of each match
def matchresults(player, computer):
    if player == computer:
        print("draw!")

    elif player == "0":
        if computer == "2":
            print("You are fire and computer is water, you lost!")
        else:
            print("You are fire and computer is grass, you won!")

    elif player == "1":
        if computer == "0":
            print("You are grass and computer is fire, you lost!")
            return -1
        else:
            print("You are grass and computer is water, you won!")

    elif player == "2":
        if computer == "1":
            print("You are water and computer is grass, you lost!")
        else:
            print("You are water and computer is fire, you won!")
            return 1

    else:
        print('You entered an invalid option, you lost!')


while True:

    computer, player = getmatchinput()

    matchresults(player, computer)
