min_ri=[]
max_le=[]
import heapq
q=int(input())
for _ in range(q):
    jdg,x,y=input().split()
    if jdg=='+':
        heapq.heappush(min_ri,int(y))
        heapq.heappush(max_le,-int(x))
    elif jdg=='-':
        if int(y)==min_ri[0]:
            min_ri.remove(int(y))
            heapq.heapify(min_ri)
        else:
            min_ri.remove(int(y))
        if -int(x)==max_le[0]:
            max_le.remove(-int(x))
            heapq.heapify(max_le)
        else:
            max_le.remove(-int(x))
    if min_ri and max_le and min_ri[0]<-max_le[0]:
        print('YES')
    else:
        print('NO')