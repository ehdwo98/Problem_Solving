from collections import deque

r,c=map(int,input().split())

arr=[]
for _ in range(r):
    arr.append(list(input()))

#print(arr)

D=[(1,0),(-1,0),(0,1),(0,-1)]
f=[]
q=deque()
for i in range(r):
    for j in range(c):
        if arr[i][j]=='J':
            q.append([i,j,'J'])#지훈 좌표 먼저 큐에 넣기
            arr[i][j]=1
        if arr[i][j]=='F':
            f.append([i,j])

if len(f)!=0:#지훈이 넣고 뒤에 불 좌표 넣기
    for i,j in f:
        q.append([i,j,'F'])
        arr[i][j]='#'

def bfs():
    while q:
        x,y,case=q.popleft()
        if x==0 or x==r-1 or y==0 or y==c-1:
            if case=='J' and arr[x][y]!='#':
                return arr[x][y]
        for dx,dy in D:
            nx,ny=x+dx,y+dy
            if 0<=nx<r and 0<=ny<c:
                if case=='F' and arr[nx][ny]!='#':#불
                    q.append([nx,ny,'F'])
                    arr[nx][ny]='#'
                elif case=='J' and arr[x][y]!='#' and arr[nx][ny]=='.':#지훈
                    q.append([nx,ny,'J'])
                    arr[nx][ny]=arr[x][y]+1
    return 'IMPOSSIBLE'

ans=bfs()
print(ans)