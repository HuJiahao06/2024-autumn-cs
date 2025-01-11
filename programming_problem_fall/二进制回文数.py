n=int(input())
m=bin(n)[2:]
cnt=0
for i in range(len(m)//2+1):
    if m[i]!=m[len(m)-i-1]:
        cnt+=1
print(['No','Yes'][cnt==0])