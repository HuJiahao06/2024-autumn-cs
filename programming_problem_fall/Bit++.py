n=int(input())
x=0

for _ in range(n):
    line=input()
    if '++' in line:
        x+=1
    elif '--' in line:
        x-=1

print(x)