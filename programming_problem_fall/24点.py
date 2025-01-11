def ans():
    lis=list(map(int,input().split()))
    cnt=0

    while True:
        if sum(lis)==24:
            cnt+=1

        for i in range(len(lis)):
            if sum(lis)-2*lis[i]==24:
                cnt+=1
            elif 2*lis[i]-sum(lis)==24:
                cnt+=1

        for j in range(len(lis)-1):
            for k in range(j+1,len(lis)):
                if sum(lis)-2*(lis[j]+lis[k])==24:
                    cnt+=1

        if cnt>0:
            print('YES')
            break
        else:
            print('NO')
            break

n=int(input())
for i in range(n):
    ans()

