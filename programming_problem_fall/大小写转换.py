s=str(input())
ans=[]

for i in s:
    if 'A' <= i <= 'Z':
        ans+=i.lower()
    elif 'a' <= i <= 'z':
        ans+=i.upper()
    else:
        ans+=i

print(''.join(ans))