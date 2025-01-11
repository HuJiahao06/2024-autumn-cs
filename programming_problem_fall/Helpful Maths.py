s=input()
cnt=s.count('+')
cnt1,cnt2,cnt3=s.count('1'),s.count('2'),s.count('3')

anslis=['1+']*cnt1+['2+']*cnt2+['3+']*cnt3

ans=''.join(anslis)

print(ans[:-1])