import sys
input=sys.stdin.readline
from collections import defaultdict

n,m=map(int,input().split())
dic=defaultdict(int)

for _ in range(n):
    i=int(input())
    for x in list(map(int,input().split())):
        dic[x]+=1
ans=0
for k,v in dic.items():
    if v>=m:
        ans+=1
print(ans)