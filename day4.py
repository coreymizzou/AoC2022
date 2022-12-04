def is_overlapping(x1,x2,y1,y2):
    return max(x1,y1) <= min(x2,y2)

def overlap(a,b,c,d):
    if (c >= a) and (c <= b) and (d >= a) and (d <= b):
        return True
    elif (a >= c) and (a <= d) and (b >= c) and (b <= d):
        return True
    else:
        return False
        
def overlapTwo(a,b,c,d):
    if (c >= a) and (c <= b) and (d >= a) and (d <= b):
        return True
    elif (a >= c) and (a <= d) and (b >= c) and (b <= d):
        return True
    elif (a == c) or (a == d) or (b == c) or (b == d):
        return True
    elif is_overlapping(a,b,c,d) == True:
        return True
    else:
        return False


f = open('input.txt')
data = f.read().splitlines()

def partOne():
    count = 0
    for line in data:
        x, y = map(str, line.split(','))
        a, b = map(int, x.split('-'))
        c, d = map(int, y.split('-'))
    
        if overlap(a,b,c,d) == True:
            count += 1

    return count
    
def partTwo():
    count = 0
    for line in data:
        x, y = map(str, line.split(','))
        a, b = map(int, x.split('-'))
        c, d = map(int, y.split('-'))
    
        if overlapTwo(a,b,c,d) == True:
            count += 1

    return count
    
    
print(partOne())
print(partTwo())
