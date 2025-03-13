import sys
input=sys.stdin.readline
from collections import deque

n=input().rstrip()
res=n
ans=0

while 1:
    res=res[-1]+str(sum(map(int,res)))[-1]
    ans+=1
    if int(res)==int(n):
        break
print(ans)
