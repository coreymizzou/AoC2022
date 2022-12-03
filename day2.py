f = open('input.txt')
data = f.read().splitlines()


def partOne():
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

    return score
    
    loss = 0 
    tie = 3
    win = 6
    
    rock = 1
    paper = 2
    scissors = 3
    
def partTwo():
    day2 = {
    "A X": 3, # verified
    "A Y": 4,  #verified
    "A Z": 8, # 6 + 2 = 8 verified
    "B X": 1, #verified
    "B Y": 5, # 3 + 2 = 5 verified
    "B Z": 9, # 6 + 3 = 9 verified
    "C X": 2, # 0 + 2 = 2 verified
    "C Y": 6, # 3 + 3 = 6 verified
    "C Z": 7 #verified
}
    score2 = 0
    for line in data:
        line = line.strip()
        score2 += day2[line]
        
    return score2


    
print(partOne())
print(partTwo())
