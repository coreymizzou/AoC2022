def overlap(a,b,c,d):
    if (c >= a) & (c <= b) & (d >= a) & (d <= b):
        return True
    elif (a >= c) & (a <= d) & (b >= c) & (b <= d):
        return True
    else:
        return False


f = open('input.txt')
data = f.read().splitlines()
count = 0

for line in data:
    x, y = map(str, line.split(','))
    a, b = map(int, x.split('-'))
    c, d = map(int, y.split('-'))
    
    if overlap(a,b,c,d) == True:
        count += 1

print(count)
