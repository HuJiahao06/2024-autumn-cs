s=input()
a,b,c,d,e=0,0,0,0,0
while True:
 for i in range(len(s)):
    a=i
    if s[i]=='h':
        e+=1
        break

 for j in range(a,len(s)):
    b=j
    if s[j]=='e':
        e+=1
        break

 for k in range(b,len(s)):
    c=k
    if s[k]=='l':
        e+=1
        break

 if c+1==len(s):
     print('NO')
     break

 for z in range(c+1,len(s)):
    d=z
    if s[z]=='l':
        e+=1
        break

 for y in range(d,len(s)):
    if s[y]=='o':
        e+=1
        break

 if e==5:
    print('YES')
    break
 else:
     print('NO')
     break