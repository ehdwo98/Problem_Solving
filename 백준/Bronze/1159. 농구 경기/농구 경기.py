import sys
input=sys.stdin.readline

n=int(input())
arr=list(input().rstrip() for _ in range(n))

dic=dict()
for a in arr:
    if a[0] not in dic:
        dic[a[0]]=1
    else:
        dic[a[0]]+=1
c=1
ans=list()
for k,v in dic.items():
    if v>=5:
        ans.append(k)
        c=0
if c:
    print('PREDAJA')
else:
    for a in sorted(ans):
        print(a,end='')