n,k,l,c,d,p,nl,np=map(int,input().split())
x=k*l//nl//n
y=c*d//n
z=p//np//n
print(min(x,y,z))