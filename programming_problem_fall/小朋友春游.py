n=int(input())
lis=[int(x) for x in input().split()]
lis1,lis2=[],[]

for i in lis:
    if i<=n:
        lis1.append(i)
    else:
        lis2.append(i)

lis11=[x for x in range(1,n+1) if x not in lis1]
lis11.sort()
lis2.sort()

print(' '.join(map(str,lis11)))
print(' '.join(map(str,lis2)))