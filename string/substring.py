#print all the substrings


s = input('Enter the string')#mock

for sv in range(0,len(s)):
    for ev in range(sv+1,len(s)+1):
        print(s[sv:ev])