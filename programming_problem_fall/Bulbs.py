n,m=map(int,input().split())
ans=set()

for _ in range(n):
    lis=list(map(int,input().split()))
    ans.update(lis[1:])

if len(ans)==m:
    print('YES')
else:
    print('NO')