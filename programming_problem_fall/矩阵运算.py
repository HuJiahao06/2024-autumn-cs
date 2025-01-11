A,B,C=[],[],[]

a,b=map(int,input().split())
for i in range(a):
    A.append(list(map(int,input().split())))

c,d=map(int,input().split())
for i in range(c):
    B.append(list(map(int,input().split())))

e,f=map(int,input().split())
for i in range(e):
    C.append(list(map(int,input().split())))

if b!=c or a!=e or d!=f:
    print('Error!')
else:
    for i in range(e):
        for j in range(f):
            C[i][j]+=sum(A[i][x]*B[x][j] for x in range(b))
    for i in range(e):
        print(*C[i])