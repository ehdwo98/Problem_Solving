import sys
input=sys.stdin.readline
from collections import deque
from copy import deepcopy


n=int(input())
gr=list(list(map(int,input().split())) for _ in range(n))

res=0
for g in gr:
    if res < max(g):
        res=max(g)

D=[(1,0),(0,1),(-1,0),(0,-1)]

ans=[]
for i in range(res):
    q=deque()
    graph=deepcopy(gr)
    cnt=0
    for r in range(n):
        for c in range(n):
            if graph[r][c]>i:
                q.append([r,c])
                while q:
                    x,y=q.popleft()
                    graph[x][y]=i
                    for dx,dy in D:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<n and 0<=ny<n and graph[nx][ny]>i:
                            q.append([nx,ny])
                            graph[nx][ny]=i
                cnt+=1
    ans.append(cnt)

print(max(ans))                    