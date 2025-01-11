a=int(input())
b=0
for i in [100,20,10,5,1]:
    b+=a//i
    a=a%i
print(b)