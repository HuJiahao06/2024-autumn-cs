def roundadd():
    num=str(input())
    print(len(num)-num.count('0'))
    list1=[]
    for i in range(len(num)):
        if num[i]!='0':
            list1.append(int(num[i])*10**(len(num)-i-1))
    print(' '.join(map(str,list1)))

t=int(input())
for _ in range(t):
    roundadd()