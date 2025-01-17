import sys
input=sys.stdin.readline
from collections import deque

a,b,c=map(int,input().split())

q=deque()
q.append([0,0])
visited=list([0]*(b+1) for _ in range(a+1))

def move(x,y):
    if not visited[x][y]:
        visited[x][y]=1
        q.append([x,y])

ans=set()
while q:
    x,y=q.popleft()
    z=c-x-y
    if x==0:
        ans.add(z)
    #a->b
    res=min(x,b-y)
    move(x-res,y+res)
    #a->c
    res=min(x,c-z)
    move(x-res,y)
    #b->a
    res=min(y,a-x)
    move(x+res,y-res)
    #b->c
    res=min(y,c-z)
    move(x,y-res)
    #c->a
    res=min(z,a-x)
    move(x+res,y)
    #c->b
    res=min(z,b-y)
    move(x,y+res)

print(*sorted(ans))