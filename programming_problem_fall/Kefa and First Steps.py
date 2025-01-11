n=int(input())
alist=list(map(int,input().split()))
alist.append(0)
ans=[]
num=1

for i in range(n):
    if alist[i]<=alist[i+1]:
        num+=1
    elif alist[i]>alist[i+1]:
        ans.append(num)
        num=1

if num>1:
    ans.append(num)

print(max(ans))