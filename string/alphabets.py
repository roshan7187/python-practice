# To print all alphabets from a to z according to the size

size = int(input('Enter the size'))#3
s='' 

for asci in range(ord('a'),ord('z')+1):
    s+=chr(asci)

for ind in range(0,len(s),size):
    print(s[ind:ind+size])

