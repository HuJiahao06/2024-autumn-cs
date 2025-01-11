N=int(input())
stu=[int(x) for x in input().split()]
dp1=[1]*N
dp2=[1]*N
for i in range(1,N):
    for j in range(i):
        if stu[j]<stu[i]:
            dp1[i]=max(dp1[i],dp1[j]+1)
#print(dp1)
max_v=dp1[-1]+dp2[-1]
for i in range(N-2,-1,-1):
    for j in range(N-1,i,-1):
        if stu[i]>stu[j]:
            dp2[i]=max(dp2[i],dp2[j]+1)
    dp1[i]+=dp2[i]
    max_v=max(max_v,dp1[i])
#print(dp2)
#print(dp1)
print(max_v-1)