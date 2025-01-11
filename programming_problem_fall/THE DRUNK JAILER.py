n=int(input())

for _ in range(n):
    numc=int(input())
    state=[0]*(numc+1)
    for i in range(1,numc+1):
        for j in range(i,numc+1,i):
            state[j]=[0,1][state[j]==0]
    ans=state.count(1)
    print(ans)