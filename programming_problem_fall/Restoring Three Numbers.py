numlist=list(map(int,input().split()))
numlist.sort()
print(numlist[3]-numlist[1],numlist[3]-numlist[0],numlist[3]-numlist[2])