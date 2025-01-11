def distri():
    n=int(input())
    if n<=2:
        print(0)
    else:
        print(n-n//2-1)

t=int(input())
for i in range(t):
    distri()