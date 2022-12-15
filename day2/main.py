def playGame(opp, player):
    score = 0
    if player == 'rock':
        score +=1
        if opp == 'scissors':
            score += 6
    elif player == 'paper':
        score += 2
        if opp == 'rock':
            score += 6
    elif player == 'scissors':
        score +=3
        if opp == 'paper':
            score += 6
    
    if opp == player:
        score += 3
    return score

def convertInput(input):
    input = input.lower()
    if input == 'a' or input == 'x':
        return "rock"
    elif input == 'b' or input == 'y':
        return 'paper'
    elif input == 'c' or input == 'z':
        return 'scissors'
    else:
        raise Exception("Invalid input")
    
with open("./advent-of-code/day2/input.txt") as f:
    finalScore = 0
    for game in f:
        opp = convertInput(game[0])
        player = convertInput(game[2])
        finalScore += playGame(opp, player)
        
print("The final score was %d" % (finalScore))
        
        