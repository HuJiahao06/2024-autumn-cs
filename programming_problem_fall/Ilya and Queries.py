s=input()
gap=0
dp=[0]

for i in range(len(s)-1):
    if s[i]==s[i+1]:
        gap+=1
    dp.append(gap)

m=int(input())
for i in range(m):
    left,right=map(int,input().split())
    ans=dp[right-1]-dp[left-1]
    print(ans)
