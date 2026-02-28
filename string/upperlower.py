s = 'AeIoU'
res = ''
ans=[]

for ch in range(ord('A'), ord('Z')+1):
    res+=chr(ch)
for ch in s:
    if ch in res:
        ans+=[chr(ord(ch)+32)]
    else:
        ans+=[ch]
        

print(ans)