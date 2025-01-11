n=int(input())
block=[set(list(input())) for _ in range(4)]
#print(block)
def dfs(x,block,ln):
    global jdg
    if x==ln-1:
        for i in range(4):
            if word[x] in block[i] and not used[i]:
                jdg+=1
                return
        return
    for i in range(4):
        if word[x] in block[i] and not used[i]:
            used[i]=1
            dfs(x+1,block,ln)
            used[i]=0
for _ in range(n):
    jdg=0
    word=input()
    ln=len(word)
    used=[0]*4
    dfs(0,block,ln)
    if jdg>0:
        print('YES')
    else:
        print('NO')