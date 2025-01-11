n,w=map(int,input().split())
v_w_lis=[]
ttlv=0

for _ in range(n):
    v_w_lis.append(list(map(int,input().split())))

v_w_lis.sort(key=lambda x:x[0]/x[1],reverse=True)
for i in range(n):
    if v_w_lis[i][1]<=w:
        ttlv+=v_w_lis[i][0]
        w-=v_w_lis[i][1]
    else:
        ttlv+=(w/v_w_lis[i][1])*v_w_lis[i][0]
        break

print(f'{ttlv:.1f}',end='\n')
