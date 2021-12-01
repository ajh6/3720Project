import requests

isWinner = False
wrongPlayer = True
wrongPoints = True
wrongWinner = True
currentPlayer = 1

print("Animal Charades!")
print("----------------")

while wrongPlayer:

    numPlayers = input("How many players? (1 - 5 & number yourselves): ")
    numPlayers = int(numPlayers)

    if numPlayers > 0 & numPlayers < 6:
        wrongPlayer = False
    else:
        print("Not in range! Pick again!")


scores = [0 for i in range(numPlayers)]


while wrongPoints:

    pointsToWin = input("How many points in order to win? (2 - 6): ")
    pointsToWin = int(pointsToWin)

    if pointsToWin > 1 & pointsToWin < 7:
        wrongPoints = False
    else:
        print("Not in range! Pick again!")


while not isWinner:

    print("\n\nPlayer " + str(currentPlayer) + ", your word is: (from api)") # MAYBE ADD TIME LIMIT

    # REQUEST RANDOM ANIMAL FROM API

    while wrongWinner:

        currentWinner = input("\nType the player's # who won: ")
        currentWinner = int(currentWinner)

        if currentWinner > 0 & currentWinner <= numPlayers:
            wrongWinner = False
        else:
            print("Not a player number! Try again!")

   
    if currentWinner == 1:
        scores[0] += 1
    if currentWinner == 2:
        scores[1] += 1
    if currentWinner == 3:
        scores[2] += 1
    if currentWinner == 4:
        scores[3] += 1
    if currentWinner == 5:
        scores[4] += 1

    for i in scores:
        if i == pointsToWin:
            isWinner = True
            print("Player " + str(i) + " won the game!")
            print("Final Scores:\n-----------")
            for i in range(numPlayers):
                print("Player " + str(i + 1) + ": " + str(scores[i]))
                

    if currentPlayer < numPlayers:
        currentPlayer += 1
    else:
        currentPlayer = 1
