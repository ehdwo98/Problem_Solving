from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph=list([0]*101 for _ in range(101))
    
    x,y=characterX*2,characterY*2
    for lx,ly,rx,ry in rectangle:
        lx,ly,rx,ry=lx*2,ly*2,rx*2,ry*2
        for i in range(lx,rx+1):
            for j in range(ly,ry+1):
                if i==lx or i==rx or j==ly or j==ry:
                    if graph[i][j]!=2:
                        graph[i][j]=1#테두리
                else:
                    graph[i][j]=2#내부
    # print(graph)
    visited=list([0]*101 for _ in range(101))
    D=[(1,0),(-1,0),(0,1),(0,-1)]
    
    q=deque()
    q.append([x,y])
    visited[x][y]=1
    while q:
        a,b=q.popleft()
        if a==itemX*2 and b==itemY*2:
            answer=visited[a][b]//2
            break
        for da,db in D:
            na,nb=a+da,b+db
            if 0<=na<101 and 0<=nb<101:
                if graph[na][nb]==1 and not visited[na][nb]:
                    q.append([na,nb])
                    visited[na][nb]=visited[a][b]+1
    
    return answer