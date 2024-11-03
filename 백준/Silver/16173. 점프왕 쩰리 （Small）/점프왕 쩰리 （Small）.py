from collections import deque
import sys
input=sys.stdin.readline

n=int(input())

graph=list(list(map(int,input().split())) for _ in range(n))
D=[(1,0),(0,1)]

q=deque()
q.append([0,0])
while q:
    x,y=q.popleft()
    v=graph[x][y]
    if v==0:
        break
    for dx,dy in D:
        nx,ny=x+dx*v,y+dy*v
        if 0<=nx<n and 0<=ny<n:
            if v==-1:
                print('HaruHaru')
                exit(0)
            q.append([nx,ny])

print('Hing')