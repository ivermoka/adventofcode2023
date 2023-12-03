file = open("2/input.txt", "r")

powerSum = 0

for line in file:
    split = line.replace(":", "").split(" ")
    
    minCubes = {"red": 0, "green": 0, "blue": 0}
    power = 1

    for i in range(2, len(split), 2):
        color = split[i+1].rstrip(",;\n")
        value = int(split[i])

        if value > minCubes[color]:
            minCubes[color] = value
        
    for items in minCubes:
        power *= minCubes[items]
    
    powerSum += power
            
print(powerSum)
   
