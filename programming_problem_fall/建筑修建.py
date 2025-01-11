#最大不重叠区间问题
def place(x,y,m):
    buf=[]
    for i in range(max(x-y+1,0),min(m,x+1)):
        if i+y<=m:
            buf.append((i,i+y))
    return buf

n,m=map(int,input().split())
plans=[(int(x) for x in input().split())for _ in range(n)]
ttl=[]
for x,y in plans:
    ttl.extend(place(x,y,m))
ttl.sort(key=lambda x: (x[1],x[0]))
cnt=0
ed=0
for st,n_ed in ttl:
    if st>=ed:
        ed=n_ed
        cnt+=1
print(cnt)