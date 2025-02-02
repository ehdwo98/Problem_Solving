import sys
input=sys.stdin.readline

n=int(input())
arr=list(input().split())

dic=dict()
for a in arr:
    tmp=list(a.split('Cheese'))
    if tmp[-1]=='':
        dic[a]=1

if sum(dic.values())>=4:
    print('yummy')
else:
    print('sad')    