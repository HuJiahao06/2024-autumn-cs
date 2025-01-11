n=int(input())
text=list(map(str,input().split()))
cnt=0
lis1=[]

for i in range(len(text)):
    if cnt+len(text[i])<=80:
        cnt+=len(text[i])+1
        lis1.append(text[i])
    elif cnt+len(text[i])>80:
        print(' '.join(lis1))
        lis1.clear()
        cnt=len(text[i])+1
        lis1.append(text[i])

print(' '.join(lis1))