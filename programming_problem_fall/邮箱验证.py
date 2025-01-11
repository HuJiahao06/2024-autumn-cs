while True:
 try:
  while True:
    s=input()
    cnt=0

    if s.count('@')!=1:
        print('NO')
        cnt+=1
        break

    if s[0]=='@' or s[-1]=='@' or s[0]=='.' or s[-1]=='.':
        print('NO')
        cnt+=1
        break

    if '.' not in s[s.index('@'):]:
        print('NO')
        cnt+=1
        break

    if s[s.index('@')-1]=='.' or s[s.index('@')+1]=='.':
        print('NO')
        cnt+=1
        break

    if cnt==0:
        print('YES')
        break
 except EOFError:
     break