n,m,k=map(int,input().split())
dp=[[-1]*(m+1) for _ in range(k+1)]
dp[0][m]=n
for i in range(k):
    qiu,hurt=map(int,input().split())
    for x in range(m):
        for y in range(i+1,0,-1):
            if x+hurt<=m and dp[y-1][x+hurt]!=-1:
                dp[y][x]=max(dp[y][x],dp[y-1][x+hurt]-qiu)
a=0
for i in range(k,-1,-1):
    for j in range(m,-1,-1):
        if dp[i][j]!=-1:
            print(i,j)
            a+=1
            break
    if a==1:break