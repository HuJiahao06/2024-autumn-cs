import heapq
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    else:
        jumping=[]
        heapq.heappush(jumping,(0,'',n))
        inq=set()
        while jumping:
            step,way,cur=heapq.heappop(jumping)
            if cur==m:
                print(step)
                print(way)
                break
            else:
                if 3*cur not in inq:
                    inq.add(3*cur)
                    heapq.heappush(jumping,(step+1,way+'H',3*cur))
                if cur//2 not in inq:
                    inq.add(cur//2)
                    heapq.heappush(jumping,(step+1,way+'O',cur//2))