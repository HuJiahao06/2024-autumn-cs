n,k=map(int,input().split())
score=list(map(int,input().split()))
num=0
for i in range(n):
    if score[i]==0:
        break
    elif score[i]>=score[k-1]:
        num+=1
print(num)