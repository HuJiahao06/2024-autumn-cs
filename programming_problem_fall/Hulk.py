n=int(input())
ans='it'

for i in range(n,0,-1):
    if i%2==0:
        ans='that I love '+ans
    elif i%2!=0:
        ans='that I hate '+ans

print(ans[5:])