import sys

input=sys.stdin.readline
n=int(input())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

#print(graph)
cnt={-1:0,0:0,1:0}

def same(n,r,c):
    for i in range(r,r+n):
        for j in range(c,c+n):
            if graph[i][j]!=graph[r][c]:
                return -2
    return graph[r][c]

def recur(n,r,c):
    res=same(n,r,c)
    if res==-1 or res==0 or res==1:
        cnt[res]+=1
        return
    recur(n//3,r,c)
    recur(n//3,r,c+n//3)
    recur(n//3,r,c+2*n//3)

    recur(n//3,r+n//3,c)
    recur(n//3,r+n//3,c+n//3)
    recur(n//3,r+n//3,c+2*n//3)
        
    recur(n//3,r+2*n//3,c)
    recur(n//3,r+2*n//3,c+n//3)
    recur(n//3,r+2*n//3,c+2*n//3)
    return

recur(n,0,0)

for c in cnt.values():
    print(c)