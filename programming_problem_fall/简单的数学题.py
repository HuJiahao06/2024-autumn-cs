t=int(input())
lis2=[pow(2,x) for x in range(0,21)]

for _ in range(t):
    n=int(input())
    gap=sum(x for x in lis2 if x<=n)
    ans=(1+n)*n//2-2*gap
    print(ans)