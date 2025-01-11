a='q w e r t y u i o p a s d f g h j k l ; z x c v b n m , . /'
keyboard=a.split()
ans=''
t=input()
line1=input()
if t=='R':
    for i in range(len(line1)):
        ans+=keyboard[keyboard.index(line1[i])-1]
    print(ans)
elif t=='L':
    for i in range(len(line1)):
        ans+=keyboard[keyboard.index(line1[i])+1]
    print(ans)