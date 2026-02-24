"""n = 5

for i in range(1, n + 1):
    for j in range(i):
        if (i + j) % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()"""

row  = 5
start = 1
for i in range(1, row + 1):
    if i % 2 == 0:
        start = 1
    else:
        start = 0
    for j in range(1, i + 1):
        print(start, end=" ")
        start = 1 - start
    
    print()















#Upper half
"""rows = 5       
for i in range(1, rows + 1,1):
    print("*" *i)

#lower half
for i in range(rows -1, 0, -1):
    print("*" *i)



for stars in range(1, 10, 2):
    spaces = (9 - stars) // 2
    print("  " * spaces + "* " * stars)




spaces = 0

for stars in range(9, 0, -2):
    print(" " * spaces + "* " * stars)
    spaces += 2

n = 11
spaces = 0

while n > 0:
    print(" " * spaces + "* " * n)
    spaces += 2
    n -= 2





rows = 5
columns = 5

for i in range(1,rows + 1):
    for j in range(1,columns + 1):
        print(i, end=" ")
    print()"""