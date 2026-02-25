# To print halo reverse triangle
'''
num = int(input('Enter the Value: '))
stars = num
for row in range(1,num+1):
    for col in range(1,stars+1):

        if row == 1 or col == 1 or row + col == num +1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#rightangled halo traingle
'''
num = int(input('Enter the Value: '))
stars = 1
spaces = num-1

for row in range(1,num+1):

    for sp in range(1,spaces+1):
        print(' ',end=' ')

    for col in range(1,stars+1):

        if row == num or col == 1 or row==col :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    spaces-=1
    stars+=1
'''

#