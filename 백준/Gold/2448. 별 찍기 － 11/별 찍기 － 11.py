n=int(input())
l=5*(n//3)+(n//3-1)
graph=[[' ']*l for _ in range(n)]
#print(graph)

def recur(n,r,c):
    if n==3:
        graph[r][c]='*'
        graph[r+1][c-1]=graph[r+1][c+1]='*'
        for i in range(-2,3):
            graph[r+2][c+i]='*'
        return
    recur(n//2,r,c)
    recur(n//2,r+n//2,c-n//2)
    recur(n//2,r+n//2,c+n//2)
    return

recur(n,0,l//2)
for g in graph:
    g=''.join(g)
    print(g)