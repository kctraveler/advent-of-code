# Converts the ASCII value the character to the scoring requirements
def scoreResult(result):
    asciiVal = ord(result)
    if asciiVal > 90:
        return asciiVal - ord('a') + 1
    else:
        return asciiVal - ord('A') + 27

with open('./advent-of-code/day3/input.txt') as f:
    finalResult = 0
    for line in f:
        line = line.rstrip()
        # convert each half of the string to a set. Find the interestion of the two sets
        compartmentOne , compartmentTwo = set(line[:len(line)//2]) , set(line[len(line)//2:])
        sharedItem = compartmentOne.intersection(compartmentTwo).pop() # we know there is only one result
        finalResult += scoreResult(sharedItem)
print('The final result value is %d' % finalResult)
  