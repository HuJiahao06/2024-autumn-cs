def match_bg(n1,boys,n2,girls):
    i,j,cnt=0,0,0
    while i<n1 and j<n2:
         if abs(boys[i]-girls[j])<=1:
             cnt+=1;i+=1;j+=1
         elif boys[i]<girls[j]-1:
             i+=1
         elif boys[i]>girls[j]+1:
             j+=1
    return cnt

n1=int(input())
boys=[int(x) for x in input().split()]
boys.sort()
n2=int(input())
girls=[int(x) for x in input().split()]
girls.sort()

print(match_bg(n1,boys,n2,girls))