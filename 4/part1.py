file = open("input.txt", "r")
points = 0

for card in file:
    currentCard = card.replace("Card", "").rstrip("\n").split("|")
    winningNumbers = list(filter(None, currentCard[0].split(" ")[2:]))
    yourNumbers = list(filter(None, currentCard[1].split(" ")))
    value = 1
    won = False
    for number in yourNumbers:
        if number in winningNumbers:
            value *= 2
            won = True
    if won: points += value
points = int(points/2)
print(points)