while True:
    N=int(input())
    if N==0:
        break
    else:
        hotels=[tuple(int(x) for x in input().split()) for _ in range(N)]
        hotels.sort()
        cnt=1
        minC=hotels[0][1]
        if N==1:
            print(1)
        else:
            for i in range(1,N):
                if hotels[i][1]<minC:
                    cnt+=1
                    minC=hotels[i][1]
            print(cnt)