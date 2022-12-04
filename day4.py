f = open('input.txt')
data = f.read().splitlines()
count = 0

for line in data:
    x, y = map(str, line.split(','))
    a, b = map(int, x.split('-'))
    c, d = map(int, y.split('-'))
    
    if (c >= a) & (c <= b) & (d >= a) & (d <= b):
        count += 1
    elif (a >= c) & (a <= d) & (b >= c) & (b <= d):
        count += 1

print(count)
