# Converts the ASCII value the character to the scoring requirements
def scoreResult(result):
    asciiVal = ord(result)
    if asciiVal > 90:
        return asciiVal - ord('a') + 1
    else:
        return asciiVal - ord('A') + 27

with open('./advent-of-code/day3/input.txt') as f:
    finalResult = 0
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        result = set(lines[i].rstrip()) & set(lines[i+1].rstrip()) & set(lines[i+2].rstrip())
        finalResult += scoreResult(result.pop())
print('The final result value is %d' % finalResult)
  