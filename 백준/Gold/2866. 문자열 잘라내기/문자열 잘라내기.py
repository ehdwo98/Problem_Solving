import sys
input=sys.stdin.readline

from collections import defaultdict

r,c=map(int,input().split())

arr=list(input().rstrip() for _ in range(r))

ans=0
s,e=0,r-1

while s<=e:
    m=(s+e)//2
    cmd=1
    dic=defaultdict(int)
    for i in range(c):
        res=''
        for j in range(m,r):
            res+=arr[j][i]
        if not dic[res]:
            dic[res]+=1
        else:
            cmd=0
            break
    if cmd:
        ans=m
        s=m+1
    else:
        e=m-1
print(ans)