from collections import deque
n,k=map(int,input().split())
nums=[int(x) for x in input().split()]
q=deque()
cu_max=-float('inf')
ans=[]
for i in range(k):
    cu_max=max(cu_max,nums[i])
    q.append(nums[i])
ans.append(cu_max)
for i in range(k,n):
    if nums[i]>=cu_max:
        cu_max=nums[i]
        ans.append(cu_max)
        q.popleft()
        q.append(nums[i])
    else:
        rmv=q.popleft()
        if rmv<cu_max:
            ans.append(cu_max)
            q.append(nums[i])
        else:
            q.append(nums[i])
            cu_max=max(q)
            ans.append(cu_max)
print(*ans)