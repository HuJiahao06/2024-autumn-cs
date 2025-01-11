import math
s=input()
n=len(s)
res=[]
ans=''
m=int(math.log(n,2))
for i in range(m+1):
    res.append(s[2**i-1])
j=0;k=len(res)-1
while j<=k:
    if j==k:
        ans+=res[j]
        break
    else:
        ans+=res[j]
        j+=1
        ans+=res[k]
        k-=1
print(ans)