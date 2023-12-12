file = open("input.txt", "r")
cardSum = 0

copies = {}
for i, card in enumerate(file):
    copies[i] = 1

file.seek(0)

for i, card in enumerate(file):
    currentCard = card.replace("Card", "").rstrip("\n").split("|")
    winningNumbers = list(filter(None, currentCard[0].split(" ")[2:]))
    yourNumbers = list(filter(None, currentCard[1].split(" ")))
    matching = 0
    for number in yourNumbers:
        if number in winningNumbers:
            matching += 1
    for j in range(copies[i]):
        for k in range(matching):
            copies[i + k + 1] += 1

sum = sum(copies.values())
print(sum)