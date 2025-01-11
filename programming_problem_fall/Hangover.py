while True:
    n=float(input())
    if n!=0.00:
        cnt = 0
        num = 0
        k = 2

        if n == 0:
            break

        while cnt < n:
            cnt += 1 / k
            num += 1
            k += 1

        print(f'{num} card(s)')

    elif n==0.00:
        break