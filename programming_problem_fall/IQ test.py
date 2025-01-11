n=int(input())
list1=list(map(int,input().split()))
odd=0
even=0
for i in list1:
    if i%2==0:
        even+=1
    else:
        odd+=1
if even>=2:
    for j in range(n):
        if list1[j]%2!=0:
            print(j+1)
            break
elif odd>=2:
    for j in range(n):
        if list1[j]%2==0:
            print(j+1)
            break