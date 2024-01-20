import sys 
sys.setrecursionlimit(10000) 

t=int(input())

D=[(-1,0),(1,0),(0,1),(0,-1)]

def dfs(y,x):
    for dy,dx in D:
        ny,nx=y+dy,x+dx
        if (m>nx>=0) and (n>ny>=0) and arr[ny][nx]==1:
            arr[ny][nx]=0
            dfs(ny,nx)

for _ in range(t):
    m,n,k=map(int,input().split())
    arr=[[0 for _ in range(m)]for _ in range(n)]
    res=0
    
    for _ in range(k):
        x,y=map(int,input().split())
        arr[y][x]=1
        
    for a in range(m):
        for b in range(n):
            if arr[b][a]==1:
                dfs(b,a)
                res+=1
                
    print(res)
