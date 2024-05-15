from collections import deque
import sys

T=int(input())

D=[(1,0),(-1,0),(0,1),(0,-1)]

for _ in range(T):
    m,n,k=map(int,input().split())

    graph=[[0]*m for _ in range(n)]

    for _ in range(k):
        x,y=map(int,sys.stdin.readline().split())
        graph[y][x]=1
    
    q=deque()
    cnt=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                q.append([i,j])
                while q:
                    y,x=q.popleft()
                    for dy,dx in D:
                        ny,nx=y+dy,x+dx
                        if 0<=ny<n and 0<=nx<m and graph[ny][nx]==1:
                            graph[ny][nx]=0
                            q.append([ny,nx])
                cnt+=1

    print(cnt)