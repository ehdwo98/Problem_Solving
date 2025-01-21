import sys
input=sys.stdin.readline
from collections import deque

def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1


T=int(input())
for _ in range(T):
    a,b=map(int,input().split())
    q=deque()
    q.append([a,0])
    visited=[0]*10000
    c=1
    while q:
        arr,cnt=q.popleft()
        visited[arr]=1
        if arr==b:
            print(cnt)
            c=0
            break
        for i in range(4):
            for j in range(10):
                res=list(str(arr))
                res[i]=str(j)
                res=int(''.join(res))
                if 1000<=res and not visited[res] and prime(res):
                    q.append([res,cnt+1])
                    visited[res]=1
    if c:
        print('Impossible')