n,a,b=map(int,input().split())
plants=[int(x) for x in input().split()]
i,j=0,n-1
cnt=0
na,nb=a,b
while i<=j:
    if i==j:
        if max(na,nb)<plants[i]:
            cnt+=1
            break
        else:
            break
    if na<plants[i]:
        cnt+=1
        na=a
        na-=plants[i]
        i+=1
    else:
        na-=plants[i]
        i+=1
    if nb<plants[j]:
        cnt+=1
        nb=b
        nb-=plants[j]
        j-=1
    else:
        nb-=plants[j]
        j-=1
print(cnt)