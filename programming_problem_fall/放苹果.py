def place(t,cases):
    max_m=max(x[0] for x in cases)
    max_n=max(x[1] for x in cases)
    dp=[[0 for _ in range(max_n+1)] for _ in range(max_m+1)]
    for m in range(max_m+1):
        dp[m][1]=1
    for n in range(max_n+1):
        dp[0][n]=1
    for m in range(1,max_m+1):
        for n in range(2,max_n+1):
            if n>m:
                dp[m][n]=dp[m][m]#盘子多于苹果
            else:
                dp[m][n]=dp[m][n-1]+dp[m-n][n]
    ans=[]
    for m,n in cases:
        ans.append(dp[m][n])
    return ans
t=int(input())
cases=[[int(x) for x in input().split()] for _ in range(t)]
result=place(t,cases)
for i in result:
    print(i)