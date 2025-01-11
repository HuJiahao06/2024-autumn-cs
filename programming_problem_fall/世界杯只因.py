n=int(input())
ai=[int(x) for x in input().split()]
ai_sight=[]
for i in range(n):
    ai_sight.append((i-ai[i],i+ai[i]))
ai_sight.sort()
st,ed=ai_sight[0]
cnt=1
for i in range(1,n):
    if ai_sight[i][0]<=0:
        ed=max(ed,ai_sight[i][1])
        if ed>=n-1:
            break
    else:
        cnt+=1
        break
buffer=ed
for i in range(1,n):
    if ai_sight[i][0]<=buffer:
        ed=max(ed,ai_sight[i][1])
        if ed>=n-1:
            break
    else:
        cnt+=1
        buffer=ed
        if ai_sight[i][0]<=buffer:
            ed=max(ed,ai_sight[i][1])
            if ed>=n-1:
                break
print(cnt)