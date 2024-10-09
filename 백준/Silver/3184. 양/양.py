import sys
sys.setrecursionlimit(10**5)

R,C=map(int,input().split())
maps=[list(input()) for _ in range(R)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

sheep, wolf, s, w =0,0,0,0

def dfs(x,y):
    global s,w
    if maps[x][y]=='v':
        w +=1
    if maps[x][y]=='o':
        s +=1
    maps[x][y]='#'
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx >= 0 and nx < R and ny >= 0 and ny < C and not maps[nx][ny]=='#':
            dfs(nx,ny)

for i in range(R):
    for j in range(C):
        if maps[i][j]!='#':
            s,w = 0, 0
            dfs(i,j)
            if s>w:
                sheep+=s
            else:
                wolf+=w

print(sheep, wolf)