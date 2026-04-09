#버튼의 최솟값 -> BFS
from collections import deque
F,S,G,U,D=map(int,input().split())
#총 F층
#스타트링크(도착장소) G
#현재 강호 S
#위로 U층씩
#아래로 D층씩

visited=[0]*(F+1)
q=deque()
q.append(S)
visited[S]=1
while q:
    p=q.popleft()
    for move in [U,-D]:
        next=p+move
        if 1<=next<=F and not visited[next]:  
            visited[next]=visited[p]+1
            q.append(next)
if visited[G]:
    print(visited[G]-1)
else:
    print("use the stairs")