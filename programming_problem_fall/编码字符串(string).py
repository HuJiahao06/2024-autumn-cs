s=str(input().lower())+'0'
cnt=1
lis=[]

for i in range(len(s)-1):
    if s[i]==s[i+1]:
        cnt+=1
    elif s[i]!=s[i+1]:
        lis.append((s[i],cnt))
        cnt=1

for _ in range(len(lis)):
    print(f'({lis[_][0]},{lis[_][1]})',end='')