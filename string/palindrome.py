s = 'malayalam'

for ind in range(0,len(s)//2):
    if s[ind] != s[-ind-1]:
        print('Not Palindrome')
        break

else:
    print('Palindrome')