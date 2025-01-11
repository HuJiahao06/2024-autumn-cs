T,M=map(int,input().split())
plants=[[int(x) for x in input().split()] for _ in range(M)]
dp=[0]*(T+1)
for i in plants:
    if T>i[0]:
        for j in range(T,i[0]-1,-1):
            dp[j]=max(dp[j],dp[j-i[0]]+i[1])
#print(dp)
print(max(dp))