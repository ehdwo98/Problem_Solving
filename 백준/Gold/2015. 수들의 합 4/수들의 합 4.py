import sys
input=sys.stdin.readline
from collections import defaultdict

n,k=map(int,input().split())

arr=list(map(int,input().split()))

s=defaultdict(int)
s[0]=1

res,ans=0,0
for a in arr:
    res+=a
    if res-k in s:
        ans+=s[res-k]
    s[res]+=1
print(ans)