import sys

input=sys.stdin.readline
n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

cnt={0:0,1:0}
def recur(n,r,c):
    curr=graph[r][c]
    for i in range(r,r+n):
        for j in range(c,c+n):
            if graph[i][j]!=curr:
                recur(n//2,r,c)
                recur(n//2,r+n//2,c)
                recur(n//2,r,c+n//2)
                recur(n//2,r+n//2,c+n//2)
                return
    cnt[curr]+=1
    return

recur(n,0,0)

for c in cnt.values():
    print(c)