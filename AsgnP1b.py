from random import randint


# Get user input for each match
def getmatchinput():
    t = ["0", "1", "2"]
    computer = t[randint(0, 2)]

    return computer, input("Enter 0(fire), 1(grass) or 2(water):")


# Calculate and display result of match
# Returns result of the match
# result : 1 for Win, 0 for Tie, -1 for Loss
def matchresults(player, computer):
    updateValue = 1
    if player == computer:
        print("draw!")
        return 0

    elif player == "0":
        if computer == "2":
            print("You are fire and computer is water, you lost!")
            return -1
        else:
            print("You are fire and computer is grass, you won!")
            return 1

    elif player == "1":
        if computer == "0":
            print("You are grass and computer is fire, you lost!")
            return -1
        else:
            print("You are grass and computer is water, you won!")
            return 1

    elif player == "2":
        if computer == "1":
            print("You are water and computer is grass, you lost!")
            return -1
        else:
            print("You are water and computer is fire, you won!")
            return 1

    else:
        print('You entered an invalid option, you lost!')
        return -1


# updateValues = [updateValue1, updateValue2, updateValue3]
def calculateRoundValues(updateValues):
    wins = 0
    loss = 0
    ties = 0
    for value in updateValues:
        if (value == -1):
            loss += 1
        elif (value == 1):
            wins += 1
        elif (value == 0):
            ties += 1
        else:
            print("something is wrong")    #shouldn't be printed but just in case, so that I know what went wrong with the code
    return wins, ties, loss


# Display final results of each round
def endofround(updateValues):
    wins, ties, loss = calculateRoundValues(updateValues)

    print('You have {0} win , {1} loss and {2} draw'.format((wins), (loss), (ties)))

    if wins > 1 or ties == 2 and wins == 1:
        print('You won the game.')

    elif ties == 3 or wins == 1 and loss == 1 and ties == 1:
        print('Tie!')

    else:
        print('You lost the game.')


while True:  # for each round

    currentRoundResults = []
    for i in range(3):  # for each match(every 3 rounds)

        computer, player = getmatchinput()

        curMatchResult = matchresults(player, computer)

        currentRoundResults.append(curMatchResult)

    endofround(currentRoundResults)


