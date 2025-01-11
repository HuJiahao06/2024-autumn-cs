lis=[x for x in range(1,100) if x%7!=0 and x%10!=7 and x//10!=7]

n=int(input())
ans=0
for k in lis:
    if k<=n:
        ans+=k**2

print(ans)