def pfact(n):
    from math import sqrt
    p_fact,num,limit=[],n,int(sqrt(n)+1)

    for i in range(2,limit):
        while num%i==0:
            p_fact.append(i)
            num/=i

    if num>1:
        p_fact.append(num)

    return p_fact

x=int(input())
if x<6 or x%2!=0:
    print('Error!')
else:
    for y in range(3,x//2+1):
        if len(pfact(y))==1 and len(pfact(x-y))==1:
            print(f'{x}={y}+{x-y}')
        else:
            continue
