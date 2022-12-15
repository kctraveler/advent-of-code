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
    if input == 'a' :
        return "rock"
    elif input == 'b' :
        return 'paper'
    elif input == 'c' :
        return 'scissors'
    else:
        raise Exception("Invalid input")
def convertPlayerMove(opp, input):  
    input = input.lower()
    if input == 'x':
        if opp == 'rock':
            return 'scissors'
        elif opp == 'paper':
            return 'rock'
        elif opp == 'scissors':
            return 'paper'
    elif input == 'y':
        return opp
    elif input == 'z':
        if opp == 'rock':
            return 'paper'
        elif opp == 'paper':
            return 'scissors'
        elif opp == 'scissors':
            return 'rock'
        
with open("./advent-of-code/day2/input.txt") as f:
    finalScore = 0
    for game in f:
        opp = convertInput(game[0])
        player = convertPlayerMove(opp,game[2])
        finalScore += playGame(opp, player)
        
print("The final score was %d" % (finalScore))
        
        