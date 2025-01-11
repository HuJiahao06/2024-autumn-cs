import heapq
N=int(input())
nums=list(map(int,input().split()))
cost=[50,100,250,500,1000,2500,5000]
heap=[]
inq=set()
heapq.heappush(heap,(0,N))
inq.add(N)
def bfs():
    while heap:
        cnt,money=heapq.heappop(heap)
        if money==0:
            return cnt
        for i in range(6,-1,-1):
            if money>=cost[i] and money-cost[i] not in inq and nums[i]>0:
                heapq.heappush(heap,(cnt+1,money-cost[i]))
                inq.add(money-cost[i])
                nums[i]-=1

    return 'Fail'
print(bfs())