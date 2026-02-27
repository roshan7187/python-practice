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
'''
# reverse rightangled triangle
num = int(input('Enter the Value: '))
stars = num
spaces = 0

for row in range(1,num+1):

    for sp in range(spaces):
        print(' ',end=' ')

    for col in range(1,stars+1):

        if row == 1 or col == 1 or row+col == num+1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    spaces+=1
    stars-=1
'''

# halo pyramid
'''
num = int(input('Enter the Value: '))
stars = 1
spaces = num-1

for row in range(1,num+1):

    for sp in range(spaces):
        print(' ',end=' ')

    for col in range(1,stars+1):

        if row == num or col == 1 or col == stars :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    spaces-=1
    stars+=2
    '''
'''
# reverse halo pyramid
num = int(input('Enter the Value: '))
stars = num*2 -1
spaces = 0

for row in range(1,num+1):

    for sp in range(spaces):
        print(' ',end=' ')

    for col in range(1,stars+1):

        if row == 1 or col == 1 or col == stars :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    spaces+=1
    stars-=2
'''
#halo diamond
'''
num = int(input('Enter the Value: '))
stars = 1
spaces = num-1

for row in range(1,num+1):

    for sp in range(spaces):
        print(' ',end=' ')

    for col in range(1,stars+1):

        if row == num or col == 1 or col == stars :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    if row < num // 2 + 1 :
        stars+=2
        spaces-=1
    else:
        stars-=2
        spaces+=1
'''

num = int(input('Enter a Value: '))
stars = num
spaces = 0

for row in range(1,num+1):
    
    for sp in range(spaces):
        print(' ',end = ' ')

    for col in range(1,stars+1):

        if row == 1 or row == num or col == 1 or col == stars:
            print('*' , end=' ')
        else:
           print(' ',end = ' ')

    print()
    if row < num//2+1:
        stars-=2
        spaces+=1
    else:
        stars+=2
        spaces-=1 
