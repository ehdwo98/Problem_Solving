from collections import deque

n,k=map(int,input().split())
SIZE=100001
arr=[0]*SIZE

q=deque()
q.append(n)
D=[1,-1,2]

def bfs():
    while q:
        x=q.popleft()
        if x==k:
            ans=arr[x]
            return ans
        for dx in D:
            if dx==2:
                nx=x*dx
            else:
                nx=x+dx
            if 0<=nx<SIZE and arr[nx]==0:
                arr[nx]=arr[x]+1
                q.append(nx)

print(bfs())