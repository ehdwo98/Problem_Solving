import sys
input=sys.stdin.readline
from collections import defaultdict

n,m,k=map(int,input().split())
dic=defaultdict(int)

for _ in range(n):
    s,p=input().split()
    p=int(p)
    dic[s]=p
    
ans=0
for _ in range(k):
    s=input().rstrip()
    ans+=dic[s]
    del dic[s]

if m==k:
    print(ans,ans)
else:
    arr=sorted(list(dic.items()),key=lambda x:x[1])
    max,min=ans,ans
    for i in range(m-k):
        max+=arr[i][1]
        min+=arr[-i-1][1]
    print(max,min)