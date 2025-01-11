n=int(input())
lis=[[int(x) for x in input().split()] for _ in range(n)]
lis.sort()
lisa=['Poor','Happy']
jdg=0
for i in range(n-1):
    if lis[i][1]<lis[i+1][1]:
        continue
    else:
        jdg+=1
        break
print(f'{lisa[jdg]} Alex')