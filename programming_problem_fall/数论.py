def pfact(n):
    from math import sqrt
    p_fact=[]
    limit=int(sqrt(n)+1)
    num=n

    for i in range(2,limit):
        while num%i==0:
            p_fact.append(i)
            num/=i

    if num>1:
        p_fact.append(num)

    return p_fact

n=pfact(int(input()))
a=0

for k in range(len(n)-1):
    if n[k]==n[k+1]:
        print(0)
        a+=1
        break

if a==0 and len(n)%2==0:
    print(1)
elif a==0 and len(n)%2!=0:
    print(-1)