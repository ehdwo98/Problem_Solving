import sys
input=sys.stdin.readline
from collections import defaultdict

dic=defaultdict(list)
n=int(input())
for _ in range(n):
    p,s=input().split()
    if s!='-':
        dic[s].append(p)

ans=[]
for k,v in dic.items():
    if len(v)==2:
        ans.append(v)
print(len(ans))
for a in ans:
    print(*a)