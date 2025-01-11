n=int(input())

for _ in range(n):
    length,num=map(int,input().split())
    ants=[int(x) for x in input().split()]
    ants.sort()
    ans2=max(ants[-1],length-ants[0])
    ans1=[]
    for i in ants:
        if i<=length/2:
            ans1.append(i)
        else:
            ans1.append(length-i)
    print(max(ans1),ans2)