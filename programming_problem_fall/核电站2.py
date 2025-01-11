N,M=map(int,input().split())
dp=[0]*(N+1)
for i in range(1,N+1):
    if i<M:
        dp[i]=2**i
    else:
        dp[i]=dp[i-1]
print(dp[N])