f = open('input.txt')
data = f.read()

total = range(len(data)-3)

for x in total:
    #print(x)
    one = data[x]
    two, three, four = data[x+1], data[x+2], data[x+3]
    firstList = [two, three, four]
    secondList = [one, three, four]
    thirdList = [one, two, four]
    fourthList = [one, two, three]
    a = any(one == c for c in firstList)
    b = any(two == c for c in secondList)
    c = any(three == c for c in thirdList)
    d = any(four == c for c in fourthList)
    
    if (a == False and b == False and c == False and d == False):
        print(four)
        print(x+4)
        break
