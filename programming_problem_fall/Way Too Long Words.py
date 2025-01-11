n=int(input())
for i in range(n):
    word=input()
    ans=''

    if len(word)>10:
        ans=f'{word[0]}{len(word)-2}{word[-1]}'
    else:
        ans=word

    print(ans)
