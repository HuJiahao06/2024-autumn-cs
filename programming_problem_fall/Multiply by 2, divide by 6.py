def into1():
    n=int(input())
    a,b=0,0

    while True:
       if n==1:
           print(0)
           break
       elif n%3!=0:
           print(-1)
           break
       else:
           while n%3==0:
              n/=3
              a+=1

           while n%2==0:
              n/=2
              b+=1

       if n!=1 or b>a:
           print(-1)
           break
       else:
           print(2*a-b)
           break

t=int(input())
for i in range(t):
    into1()


