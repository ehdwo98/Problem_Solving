from collections import deque

n,m=map(int,input().split())

arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

D=[(1,0),(-1,0),(0,1),(0,-1)]

ans=[]

for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            arr[i][j]=0
            q=deque()
            q.append([i,j])
            w=1
            while q:
                x,y=q.pop()
                for dx,dy in D:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<n and 0<=ny<m and arr[nx][ny]==1:
                        arr[nx][ny]=0
                        q.append([nx,ny])
                        w+=1
            ans.append(w)

print(len(ans))
if len(ans)==0:
    print(0)
else:
    ans.sort()
    print(ans[-1])