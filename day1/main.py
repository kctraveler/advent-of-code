maxCalories = [0,0,0]
with open("./advent-of-code/day1/input.txt") as f:
    elfCalories = 0
    for line in f:
        try:
            elfCalories += int(line)           
        except:
            #Triggered by blank line value error
            if elfCalories > maxCalories[0]:
                maxCalories.append(elfCalories)
                maxCalories.sort()
                maxCalories.pop(0)
                
            elfCalories = 0
print("The sum of top 3 calories carried is: %d" % (sum(maxCalories)))
