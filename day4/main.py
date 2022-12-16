result = 0
with open('./advent-of-code/day4/input.txt') as f:
    for line in f:
        elfRanges = line.rstrip().split(",")
        elfOne, elfTwo = tuple(map(int, elfRanges[0].split("-"))), tuple(map(int,elfRanges[1].split("-")))
        # check if elfOne contained by elfTwo
        if (elfOne[0] >= elfTwo[0] and elfOne[0] <= elfTwo[-1]) and ( elfOne[-1] <= elfTwo[-1]):
            result +=1
        # Check if elfTwo contained by elfOne
        elif (elfTwo[0] >= elfOne[0] and elfTwo[0] <= elfOne[-1]) and (elfTwo[-1] <= elfOne[-1]):
            result +=1 
print("Number of groups that completely overlap: %d" % result)