def odivisor():
    n=int(input())
    while True:
        n=n/2
        if n%2!=0 and n>1:
            print('YES')
            break
        elif n==1:
            print('NO')
            break

t=int(input())
for i in range(t):
    odivisor()