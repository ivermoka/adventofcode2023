file = open("1\input.txt", "r")

numbersSum = []

for line in file:
    numbers = []
    for letter in line:
        if letter.isdigit():
            numbers.append(letter)
    numbersSum.append(int(numbers[0] + numbers[len(numbers)-1]))

file.close()

print(sum(numbersSum))



    