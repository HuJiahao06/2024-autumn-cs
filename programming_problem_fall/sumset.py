N=int(input())
nums=[]
i=1
while i<=N:
    nums.append(i)
    i*=2

dp=[1]+[0]*N
for j in nums:
    for i in range(1,N+1):
        if i>=j:
            dp[i]=(dp[i]+dp[i-j])%(10**9)

print(dp[N])