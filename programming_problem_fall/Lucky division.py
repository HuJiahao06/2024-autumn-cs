luckylis=[4,7,44,47,74,77,444,447,474,744,477,747,774,777]
n=int(input())
while True:
    if n in luckylis:
        print('YES')
        break

    for i in luckylis:
        if n%i==0:
            print('YES')
            n=0
            break
        else:
            continue

    if n!=0:
        print('NO')
        break
    else:
        break