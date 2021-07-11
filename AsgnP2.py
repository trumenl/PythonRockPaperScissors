from random import randint


# Get user input for the amount they would like to bet
def getbet(points, void):
    while True:
        bet = int(input(
            "You have {0} points and {1} void chance.\n Enter the number of points to be used for next game: ".format(
                (points), (void))))
        if bet <= 0 or bet > points:        #if user inputs invalid number
            print('You do not have enough points')
        else:
            break
    return bet


# Get user input for each match
def getmatchinput():
    t = ["0", "1", "2"]
    computer = t[randint(0, 2)]        #computer's randomly selected number

    return computer, input("Enter 0(fire), 1(grass) or 2(water):")


# Calculate and display result of match
# Returns result of the match
# result : 1 for Win, 0 for Tie, -1 for Loss, 2 for Void
def matchresults(player, computer, void):
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

    elif (player == "V" and void > 0) or (player == "v" and void > 0):
        print('Your game is void')
        return 2
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
            print("something is wrong",
                  value)  # shouldn't be printed but just in case, so that I know what went wrong with the code
    return wins, ties, loss


# Display final results of each round
def endofround(bet, points, updateValues):
    newpoints = points

    if (len(updateValues) == 0):
        return points

    wins, ties, loss = calculateRoundValues(updateValues)

    print('You have {0} win , {1} loss and {2} draw'.format((wins), (loss), (ties)))
    if wins > 1 or ties == 2 and wins == 1:
        newpoints += bet
        print('You won the game with {0} points added'.format((bet)))
    elif ties == 3 or wins == 1 and loss == 1 and ties == 1:
        print('Tie! Your points remain unchanged.')
    else:
        newpoints -= bet
        print('You lost the game and with {0} points deducted'.format((bet)))

    return newpoints


def startgame():
    points = 10  # set orginal starting points
    void = 1  # set number of void chances
    counter = []  # list to store each match's results to compute winning streak
    streak = 0

    while True:  # for each round
        bet = getbet(points, void)

        currentRoundResults = []
        for i in range(3):  # for each match (every 3 rounds)

            computer, player = getmatchinput()

            if player == "-1":  # for player to quit the game
                print('Game ended.')
                break

            curMatchResult = matchresults(player, computer, void)
            if (curMatchResult == 1):           #wins=1, draws/losses =0, putting them in counter list to compute winning streak later on
                counter.append(1)
            elif (curMatchResult == 0 or curMatchResult == -1):
                counter.append(0)

            if curMatchResult == 2:  # if player choose to void game
                currentRoundResults = []
                void -= 1
                break
            currentRoundResults.append(curMatchResult)

        ################
        if player == "-1":  # player quits game
            break

        points = endofround(bet, points, currentRoundResults)

        if points == 0:
            print("You have no more points. End of game!")
            streak = winningstreak(counter)  # call winningstreak function
            break

    return streak


def winningstreak(counter):  # To compute winning streak
    count = 0
    streak = 0
    for x in counter:
        if (x == 0):
            count = 0
        else:
            count += 1
            if (count > streak):
                streak = count

    print('Your longest winning streak is {} '.format((streak)))
    return streak


def getContinueGame():    #for user to choose whether to start a new game or to end it
    while (True):
        res = input("Do you want to start a new game? (Y/N):")
        if (res == "Y" or res == "y"):
            return True
        if (res == "N" or res == "n"):
            return False


def updateLeaderboard(leaderboard, name, streak):
    found = False
    for i in range(len(leaderboard)):
        if (leaderboard[i][1] <= streak):
            leaderboard.insert(i, (name, streak))
            found = True
            break

    if (not found):
        leaderboard.append((name, streak))

    if len(leaderboard) > 10:      #to display only top 10 player's results
        return leaderboard[:10]
    return leaderboard


def printLeaderboard():
    print("Leaderboard -----------------------------")
    for i in range(len(leaderboard)):
        name = leaderboard[i][0]
        score = leaderboard[i][1]
        print(str(i + 1) + ". " + name + ": " + str(score))


leaderboard = []
gameHasNotEnd = True

while (gameHasNotEnd):
    name = input("Enter your player name:")       #get player name
    streak = startgame()
    leaderboard = updateLeaderboard(leaderboard, name, streak)
    printLeaderboard()
    gameHasNotEnd = getContinueGame()
