position=str(input())
cnt=1
for i in range(len(position)-1):
    if position[i]==position[i+1]:
        cnt+=1
    elif position[i]!=position[i+1]:
        cnt=1
    if cnt==7:
        print('YES')
        break
if cnt<7:
    print('NO')