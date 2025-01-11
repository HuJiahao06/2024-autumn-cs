n=int(input())
ratings=[int(x) for x in input().split()]
dp0=[1]*n
dp1=[1]*n
for i in range(1,n):
    if ratings[i]>ratings[i-1]:
        dp0[i]=dp0[i-1]+1
dp1[-1]=max(dp1[-1],dp0[-1])
for i in range(n-2,-1,-1):
    if ratings[i]>ratings[i+1]:
        dp1[i]=max(dp0[i],dp1[i+1]+1)
    else:
        dp1[i]=max(dp1[i],dp0[i])
print(sum(dp1))