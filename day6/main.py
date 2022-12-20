def identifyFrame(input, frameSize=4):
    input = list(input)
    frame = list(input[0])
    i = 1
    while i < len(input):
        if input[i] in frame: #duplicate found, shift the frame
            for j in range(frame.index(input[i])+1):
                frame.remove(frame[0])
            frame.append(input[i])
            i+=1
        elif len(frame) < frameSize - 1 : # frame too short, add the element
            frame.append(input[i])
            i+=1
        else: #frame found return the index
            return i + 1

def main():
    with open("./advent-of-code/day6/input.txt") as f:
        input = f.read()
    print(identifyFrame(input, 14))
    
main()