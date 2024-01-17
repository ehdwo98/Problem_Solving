from sys import stdin
from collections import deque
input=stdin.readline

n=int(input())
q=deque()

for _ in range(n):
    arr=list(input().split())
    
    if arr[0]=='push_front':
        c,n=arr
        q.appendleft(n)
    elif arr[0]=='push_back':
        c,n=arr
        q.append(n)
    elif arr[0]=='pop_front':
        if len(q)==0:
            print(-1)
        else:
            p=q.popleft()
            print(p)
    elif arr[0]=='pop_back':
        if len(q)==0:
            print(-1)
        else:
            p=q.pop()
            print(p)
    elif arr[0]=='size':
        print(len(q))
    elif arr[0]=='empty':
        if len(q)==0:
            print('1')
        else:
            print('0')
    elif arr[0]=='front':
        if len(q)==0:
            print('-1')
        else:
            print(q[0])
    elif arr[0]=='back':
        if len(q)==0:
            print('-1')
        else:
            print(q[-1])