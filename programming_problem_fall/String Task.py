s=input()
ans=''

for i in s:
    if i!='a' and i!='e' and i!='i' and i!='o' and i!='u' and i!='y' and i!='A' and i!='E' and i!='I' and i!='O' and i!='U' and i!='Y':
        if i<'a':
            ans+=f'.{chr(ord(i)+32)}'
        elif i>'a':
            ans+=f'.{i}'

print(ans)