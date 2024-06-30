n=int(input())

graph=[[' ']*n for _ in range(n)]
#print(graph)

def recur(n,r,c):
    if n==1:
        graph[r][c]='*'
        return
    recur(n//3,r,c)
    recur(n//3,r,c+n//3)
    recur(n//3,r,c+2*n//3)

    recur(n//3,r+n//3,c)
    #공백
    recur(n//3,r+n//3,c+2*n//3)

    recur(n//3,r+2*n//3,c)
    recur(n//3,r+2*n//3,c+n//3)
    recur(n//3,r+2*n//3,c+2*n//3)

recur(n,0,0)
for g in graph:
    g=''.join(g)
    print(g)