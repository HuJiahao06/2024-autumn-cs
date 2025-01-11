import math

while True:
    try:
       m,n=map(int,input().split())
       a=math.gcd(m,n)
       print(a)
    except EOFError:
        break