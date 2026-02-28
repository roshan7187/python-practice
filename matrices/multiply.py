m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[9,8,7],[6,5,4],[3,2,1]]
ans = []

if len(m1) == 0 or len(m2) == 0:
    print(ans)

elif len(m1) > 0 and len(m2) > 0 and len(m1[0]) == len(m2):
    for ind1 in range(len(m1)):
        line = []
        for ind2 in range(len(m2[0])):
            ele = 0
            for ind3 in range(len(m2)):
                ele = ele + m1[ind1][ind3] * m2[ind3][ind2]
            line.append(ele)
        ans.append(line)
    print(ans)

else:
    print('Matrices cannot be multiplied')