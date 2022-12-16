
def createCave(input):
    walls = list()
    for line in input:
        line.rstrip("\n")
        walls.append(line.split(' -> '))
    
    max_X = max_Y = 0
    for wall in walls:
        for corner in wall:
            corner = tuple(map(int,corner.split(","))) #extract coordinate
            max_X = corner[0] if corner[0] > max_X else max_X
            max_Y = corner[-1] if corner[-1] > max_Y else max_Y
    cave = [["."]*max_Y]*max_X
    print("Cave width: %d\nCave depth: %d\n" % (len(cave), len(cave[0])))
    return cave;

def generateWall(cave, wall):
    while i < len(wall) :
        
        
        i += 1
        
        
        
     
    
def main():
    with open("./advent-of-code/day14/input.txt") as f:
        lines = f.read().splitlines()
    cave = createCave(lines)


main()