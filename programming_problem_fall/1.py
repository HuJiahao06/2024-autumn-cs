t=int(input())
for _ in range(t):
    n=int(input())
    ans=(n+1)*n//2
    cnt=0
    while n>=2:
        cnt+=1
        n/=2
    ans-=2*(2**(cnt+1)-1)
    print(int(ans))