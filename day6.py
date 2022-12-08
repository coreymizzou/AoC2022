f = open('input.txt')
data = f.read()

total = range(len(data) - 3)

for x in total:
    y = 0
    if (data[x+3] != data[x+2]) or (data[x+3] != data[x+1]) or (data[x+3] != data[x+1]):
        print(x)
