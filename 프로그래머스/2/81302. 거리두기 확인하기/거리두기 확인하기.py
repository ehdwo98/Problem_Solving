from collections import deque

def solution(places):
    answer = []
    n=5
    D=([1,0],[0,1],[-1,0],[0,-1])
    for place in places:
        cmd=0
        for i in range(n):
            for j in range(n):
                if place[i][j]=='P':
                    visited=[[0]*n for _ in range(n)]
                    q=deque()
                    q.append([i,j,0])
                    visited[i][j]=1
                    while q:
                        x,y,cnt=q.popleft()
                        if cnt>2:
                            continue
                        for dx,dy in D:
                            nx,ny=x+dx,y+dy
                            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                                if place[nx][ny]=="O":
                                    visited[nx][ny]=1
                                    q.append([nx,ny,cnt+1])
                                elif place[nx][ny]=="P":
                                    if cnt<2:
                                        # print([x,y],[nx,ny],cnt)
                                        cmd=1
                                        break
                        if cmd:
                            answer.append(0)
                            break
                if cmd:
                    break
            if cmd:
                break
        if not cmd:
            answer.append(1)
                    
    return answer