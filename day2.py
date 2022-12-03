f = open('input.txt')
data = f.read().splitlines()

day2 = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}


score = 0
for line in data:
    line = line.strip()
    score += day2[line]

print(score)
