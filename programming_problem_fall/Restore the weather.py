def resweather():

    n,k=map(int,input().split())
    an=list(map(int,input().split()))
    bn=list(map(int,input().split()))
    an1=[(an[i],i) for i in range (n)]
    bn.sort()
    an1.sort()

    lis1=[0]*n
    for j in range(n):
        lis1[an1[j][1]]=bn[j]
    print(' '.join(map(str,lis1)))


t=int(input())
for _ in range(t):
    resweather()