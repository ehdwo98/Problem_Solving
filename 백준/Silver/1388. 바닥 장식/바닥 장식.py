import sys
input=sys.stdin.readline
from collections import deque

n,m=map(int,input().split())
arr=list(list(input().rstrip())for _ in range(n))
ans=0
for i in range(n):
    for j in range(m):
        if arr[i][j]!='#':
            q=deque()
            q.append([i,j])
            while q:
                x,y=q.popleft()
                if arr[x][y]=='-':
                    arr[x][y]='#'
                    if y+1<m and arr[x][y+1]=='-':
                        q.append([x,y+1])
                elif arr[x][y]=='|':
                    arr[x][y]='#'
                    if x+1<n and arr[x+1][y]=='|':
                        q.append([x+1,y])
            ans+=1
print(ans)