file = open("1\input.txt", "r")

numbersSum = []
textNumbers = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}
for line in file:
    numbers = []
    for key, value in textNumbers.items():
        line = line.replace(key, value)
    for letter in line:
        if letter.isdigit():
            numbers.append(letter)
        
    numbersSum.append(int(numbers[0] + numbers[len(numbers)-1]))

file.close()

print(sum(numbersSum))



    