f = open('input.txt')
data = f.read().splitlines()



priorities = 0
for i in data:
    middle = len(i) // 2
    a, b = i[:middle], i[middle:]
    
    my_str = ''
    for w in set(a):
        if w in b:
            my_str += w
    print(my_str)
