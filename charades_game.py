import requests

isWinner = False
wrongPlayer = True
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

response = requests.get("http://www.randomnumberapi.com/api/v1.0/random?min=2&max=6&count=1")
pointsToWin = response.text[1]
print("Number of points needed to win the game: " + pointsToWin)


while not isWinner:

    response = requests.get("https://random-word-form.herokuapp.com/random/animal")
    animal = response.json()[0]

    print("\n\nPlayer " + str(currentPlayer) + ", your word is: " + animal + "\n\n") # MAYBE ADD TIME LIMIT

    # REQUEST RANDOM ANIMAL FROM API

    while wrongWinner:

        currentWinner = input("\nType the player's # who won (or 0 to skip animal and draw again): ")
        currentWinner = int(currentWinner)

        if currentWinner > 0 & currentWinner <= numPlayers:
            wrongWinner = False
        elif currentWinner == 0:
            print("Redrawing Animal...")
            wrongWinner = False
        else:
            print("Not a player number! Try again!")
    wrongWinner = True
   
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

    if currentWinner != 0:
        if currentPlayer < numPlayers:
            currentPlayer += 1
        else:
            currentPlayer = 1
