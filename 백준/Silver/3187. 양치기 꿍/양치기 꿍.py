import sys
input=sys.stdin.readline
from collections import deque

r,c=map(int,input().split())
graph=list(list(input().rstrip()) for _ in range(r))
visited=list([0]*c for _ in range(r))
D=[(1,0),(-1,0),(0,1),(0,-1)]

ans_v,ans_k=0,0
for i in range(r):
    for j in range(c):
        if (graph[i][j]=='v' or graph[i][j]=='k') and visited[i][j]==0 :
            q=deque()
            q.append([i,j])
            cnt_v,cnt_k=0,0
            while q:
                x,y=q.popleft()
                visited[x][y]=1
                if graph[x][y]=='v':
                    cnt_v+=1
                elif graph[x][y]=='k':
                    cnt_k+=1
                for dx,dy in D:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<r and 0<=ny<c and graph[nx][ny]!='#' and not visited[nx][ny]:
                        q.append([nx,ny])
                        visited[nx][ny]=1
            if cnt_v<cnt_k:
                cnt_v=0
            else:
                cnt_k=0
            ans_v+=cnt_v
            ans_k+=cnt_k

print(ans_k, ans_v)