from collections import deque

n,m=map(int,input().split())

graph=[]
for _ in range(m):
    graph.append(list(map(int,input().split())))

#print(graph)

D=[(1,0),(-1,0),(0,1),(0,-1)]

def bfs():
    cnt=0
    q=deque()
    for i in range(m):
        for j in range(n):
            if graph[i][j]==1:
                q.append([i,j])
    while q:
        x,y=q.popleft()
        for dx,dy in D:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and graph[nx][ny]==0:
              q.append([nx,ny])
              graph[nx][ny]=graph[x][y]+1
              cnt+=1
    
    for g in graph:
        if 0 in g:
            print(-1)#익지 않은 토마토가 있을 경우
            return
        else:
            g.sort(reverse=True)
    graph.sort(reverse=True)
    if cnt==0:
        print(0)#익지 않은 토마토 조건 뒤에 위치해야 -1가 섞여있을 때도 0으로 출력 가능
        return
    
    print(graph[0][0]-1)
    return

bfs()