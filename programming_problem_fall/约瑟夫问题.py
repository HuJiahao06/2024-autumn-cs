while True:
    n,m=map(int,input().split())
    if n+m==0:
        break
    else:
        jdg=[1]*n
        cnt=0;k=1
        while jdg.count(1)!=1:
            if jdg[cnt%n]:
                if k<m:
                    k+=1
                    cnt+=1
                    continue
                elif k==m:
                    jdg[cnt%n]=0
                    k=1
                    cnt+=1
                    continue
            else:
                cnt+=1
                continue
        print(jdg.index(1)+1)
