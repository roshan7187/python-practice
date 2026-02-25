#Check the given strings are anagrams or not

s1=input('Enter the s1: ')#listen
s2=input('Enter the s2: ')#silent

if len(s1) == len(s2):
    for ch in s1:
        if s1.count(ch) != s2.count(ch):
            print('Not Anagram')
            break
    else:
        print('Anagram')

else:
    print('Not Anagram')
