n=int(input())
for _ in range(n):
    a=int(input())
    if a%19==0:
        print('Yes')
    elif '19' in str(a):
        print('Yes')
    else:
        print('No')