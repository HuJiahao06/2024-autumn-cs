def summ():
    a,b,c=map(int,input().split())
    if a+b+c==2*max(a,b,c):
        print('YES')
    else:
        print('NO')

t=int(input())
for _ in range(t):
    summ()