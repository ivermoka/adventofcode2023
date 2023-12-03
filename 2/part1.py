file = open("2/input.txt", "r")

possibleGames = []

for line in file:
    split = line.split(" ")
    flag = False
    for item in split:
        if item.isdigit():
            color = split[split.index(item)+1].rstrip(",;")
            if color == "red" and int(item) > 12:
                flag = True
                break
            elif color == "green" and int(item) > 13:
                flag = True
                break
            elif color == "blue" and int(item) > 14:
                flag = True
                break
    if not flag:
        possibleGames.append(int(split[1].replace(":", "")))

                    
            
print(sum(possibleGames))
   
