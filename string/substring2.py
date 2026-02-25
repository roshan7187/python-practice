# To print the substring which are palindrome

s=input('Enter the String: ')#malayalam
L =[]
for sv in range(0,len(s)):
    for ev in range(sv+1,len(s)+1):
        word = s[sv:ev]
        if word == word[::-1]:

            L.append(word)
print(L)