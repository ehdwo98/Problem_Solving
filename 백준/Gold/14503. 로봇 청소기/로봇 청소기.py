n,m=map(int,input().split())
r,c,d=map(int,input().split())

D=[[-1,0],[0,1],[1,0],[0,-1]]

graph=list(list(map(int,input().split())) for _ in range(n))
cleaned=list([0]*(m) for _ in range(n))

cnt=0
while 1:
    if not cleaned[r][c]:
        cleaned[r][c]=1
        cnt+=1
    moved=1
    for _ in range(4):
        d=(d+3)%4
        dr,dc=D[d][0],D[d][1]
        nr,nc=r+dr,c+dc
        if 0<=nr<n and 0<=nc<m:
            if graph[nr][nc]==0 and not cleaned[nr][nc]:
                r,c=nr,nc
                moved=0
                break
    if moved:
        br,bc=r-dr,c-dc
        if 0<=br<n and 0<=bc<m and not graph[br][bc]:
            r,c=br,bc
        else:
            break
print(cnt)