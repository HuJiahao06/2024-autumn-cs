num=int(input())
color=str(input())
a=0
for i in range(num-1):
    if (color[i])==(color[i+1]):
        a+=1
print(a)