m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[9,8,7],[6,5,4],[3,2,1]]

if len(m1) == 0 or len(m2) == 0:
    print(m1)

elif len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
    for ind1 in range(len(m1)):
        for ind2 in range(len(m1[0])):
            m1[ind1][ind2] = m1[ind1][ind2] + m2[ind1][ind2]
    print(m1)

else: 
    print('Matrices cannot be added')