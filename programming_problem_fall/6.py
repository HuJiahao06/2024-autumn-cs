n = int(input())
for _ in range(n):
    normal = set()
    abn = set()
    cases = [[x for x in input().split()] for _ in range(3)]

    for i in range(3):
        if cases[i][2] == 'even':
            for j in range(len(cases[0][0])):
                normal.add(cases[i][0][j])
                normal.add(cases[i][1][j])
        else:
            for j in range(len(cases[0][0])):
                abn.add(cases[i][0][j])
                abn.add(cases[i][1][j])

    for i in abn - normal:
        ans = i

    for i in cases:
        if i[2] == 'up':
            if ans in i[0]:
                print(f'{ans} is the counterfeit coin and it is heavy.')
            elif ans in i[1]:
                print(f'{ans} is the counterfeit coin and it is light.')
            break
        elif i[2] == 'down':
            if ans in i[0]:
                print(f'{ans} is the counterfeit coin and it is light.')
            elif ans in i[1]:
                print(f'{ans} is the counterfeit coin and it is heavy.')
            break