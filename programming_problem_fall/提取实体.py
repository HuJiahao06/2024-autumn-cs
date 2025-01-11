n=int(input())
cnt=0

for i in range(n):
    lis=list(input().split())
    lis.append('0')

    for j in range(len(lis)-1):
        if '###' in lis[j]:
            cnt+=1
        if '###' in lis[j] and '###' in lis[j+1]:
            cnt-=1

    lis.clear()

print(cnt)