import sys
from collections import deque
input=sys.stdin.readline
n=int(input())

que=deque()

def push(X):
    que.append(X)

def pop():
    if len(que)==0:
        print(-1)
    else:
        p=que.popleft()
        print(p)

def size():
    print(len(que))

def empty():
    if len(que)==0:
        print(1)
    else:
        print(0)

def front():
    if len(que)==0:
        print(-1)
    else:
        print(que[0])

def back():
    if len(que)==0:
        print(-1)
    else:
        print(que[-1])

for _ in range(n):
    c=list(input().split())
    #print(c)
    if len(c)!=1:
        X=int(c[1])
    c=c[0]
    if c=='push':
        push(X)
    elif c=='pop':
        pop()
    elif c=='size':
        size()
    elif c=='empty':
        empty()
    elif c=='front':
        front()
    elif c=='back':
        back()