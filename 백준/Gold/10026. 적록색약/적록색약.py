from collections import deque

n=int(input())

graph=[]
for _ in range(n):
    graph.append(list(input()))

D=[(1,0),(-1,0),(0,1),(0,-1)]

q=deque()
q2=deque()
q3=deque()
q4=deque()
cnt=0
cnt2=0
cnt3=0
cnt4=0
for i in range(n):
    for j in range(n):
        if graph[i][j]=='B':
            q.append([i,j])
            graph[i][j]='b'
            while q:
                x,y=q.popleft()
                for dx,dy in D:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny]=='B':
                            graph[nx][ny]='b'
                            q.append([nx,ny])
            cnt+=1

        elif graph[i][j]=='R':
            q2.append([i,j])
            graph[i][j]='r'
            while q2:
                x,y=q2.popleft()
                for dx,dy in D:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny]=='R':
                            graph[nx][ny]='r'
                            q2.append([nx,ny])
            cnt2+=1

        elif graph[i][j]=='G':
            q3.append([i,j])
            graph[i][j]='g'
            while q3:
                x,y=q3.popleft()
                for dx,dy in D:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny]=='G':
                            graph[nx][ny]='g'
                            q3.append([nx,ny])
            cnt3+=1

for i in range(n):
    for j in range(n):
        if graph[i][j]=='r' or graph[i][j]=='g':
            q4.append([i,j])
            graph[i][j]='#'
            while q4:
                x,y=q4.popleft()
                for dx,dy in D:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny]=='r' or graph[nx][ny]=='g':
                            graph[nx][ny]='#'
                            q4.append([nx,ny])
            cnt4+=1

print(cnt+cnt2+cnt3,cnt+cnt4)