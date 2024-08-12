rows = 6 
for i in range(rows):
    for j in range(i):
        print(i, end='')
    print('')


row = 5 
b = 0
for i in range(rows,0,-1):
    b +=1
    for j in range(1, i + 1):
        print(b, end='')
    print('')    