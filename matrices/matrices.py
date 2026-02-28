

rows = 3
cols = 3
L = []

for rows in range(1,rows+1):
    ele = []
    for col in range(1,cols+1):
        ele = ele + [eval(input('Enter Values: '))]
    L.append(ele)
print(L)