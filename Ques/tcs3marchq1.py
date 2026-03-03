L = int(input())
R = int(input())

def palindrome(num):
    return str(num) == str(num)[::-1]

def no_repeated_digits(num):
    s = str(num)
    return len(set(s)) == len(s)

result = []

for num in range(L, R + 1):
    if (num % 7 == 0 and 
        num % 5 != 0 and 
        not palindrome(num) and 
        no_repeated_digits(num)):
        result.append(str(num))

if result:
    print(" ".join(result))
else:
    print(-1)