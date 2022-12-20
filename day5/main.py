import re  

# Create the stacks structure
def parseCrates(crates):
    #setup the stacks based on last row of input
    stacks = []
    stackList = crates.pop().strip("")
    for char in stackList:
        if char.isalnum():
            stacks.append(list())
    #populate the stacks
    for row in crates:
        i = 1
        stackNumber = 0
        height = 0
        while i < len(row):
            if(not(row[i:i+1].isspace( ))):
                stacks[stackNumber].insert(height,row[i:i+1])
            stackNumber +=1
            i+= 4
        height+=1
    return stacks

#Update to move multiple crates at once
def moveCrate(source, dest, stacks, numCrates=1):
    #subtract 1 to find the index for requested move
    source, dest, numCrates = int(source), int(dest), int(numCrates)
    source-=1
    dest-=1
    toMove = list()
    for i in range(numCrates):
        toMove.append(stacks[source].pop())
    toMove.reverse()
    stacks[dest].extend(toMove)
 
#interpret a complete instruction calls moveCrate   
def doInstruction(instruction, stacks):
    steps = re.sub("[^0-9]+", "!", instruction).split("!")
    steps.pop(0)
    moveCrate(steps[1], steps[2], stacks, steps[0])
  
#Generate the result    
def printTopCrates(stacks):
    for stack in stacks:
        print(stack[-1],end="")
    print("\n")
    
def main():
   #Take the input and split it up into its parts. crates and instructions
    with open('./advent-of-code/day5/input.txt') as f:
        input = f.read()
    crates = input.split("\n\n")[0].split('\n')
    instructions = input.split("\n\n")[1].split("\n")
    stacks = parseCrates(crates)
    for instruction in instructions:  
        doInstruction(instruction, stacks)
    printTopCrates(stacks)
    
main()


