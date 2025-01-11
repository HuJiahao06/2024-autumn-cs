def zeller():
    date=str(input())
    c,y,m,d=int(date[0:2]),int(date[2:4]),int(date[4:6]),int(date[6:])
    if m<=2:
        m+=12
        y-=1
    if date[2:4]=='00' and m>=13:
        c-=1
        y=99

    w=(y+int(y/4)+int(c/4)-2*c+int(26*(m+1)/10)+d-1)%7

    if w==0:
        print('Sunday')
    elif w==1:
        print('Monday')
    elif w==2:
        print('Tuesday')
    elif w==3:
        print('Wednesday')
    elif w==4:
        print('Thursday')
    elif w==5:
        print('Friday')
    elif w==6:
        print('Saturday')

n=int(input())
for i in range(n):
    zeller()