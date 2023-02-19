N=int(input())

maps=[list(map(int,input())) for _ in range(N)]
visit=[[0]*N for _ in range(N)]

D=[[1,0],[-1,0],[0,1],[0,-1]]

num=[]
cnt=0
def dfs(x,y):
    if 0<=x<N and 0<=y<N and maps[x][y]==1:
        global cnt
        cnt+=1
        maps[x][y]=0
        for i,j in D:
            nx,ny=x+i,y+j
            dfs(nx,ny)
        return True
    return False
    
for i in range(N):
    for j in range(N):
        if dfs(i,j)==True:
            num.append(cnt)
            cnt=0

num.sort()
print(len(num))
for i in num:
    print(i)