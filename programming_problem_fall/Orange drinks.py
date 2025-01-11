n=int(input())
drinks=list(map(int,input().split()))
total=0
for i in range(n):
    total+=drinks[i]
print(total/n)